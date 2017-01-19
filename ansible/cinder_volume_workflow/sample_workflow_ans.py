#!/usr/bin/python
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
from cinderclient import client as ciclient
from novaclient import client as nova_c

#Depending upon the access assign role to user and add to the group
def access_role(user,project,access,keystone):
    ru = keystone.roles.find(name="user")
    rd = keystone.roles.find(name="vol_del")
    gru = keystone.groups.find(name="cinder_delete")
    if access == "all_volume_operations":
        keystone.roles.grant(ru,user=user,project=project)
        keystone.roles.grant(rd,user=user,project=project)
        keystone.users.add_to_group(user, gru)
    elif access == "all_volume_operations_except_delete":
        keystone.roles.grant(ru,user=user,project=project)
    elif access == "only_volume_delete":
        keystone.roles.grant(rd,user=user,project=project)
        keystone.users.add_to_group(user, gru)

def validate_as_admin(usr,prj, passwd, role):
#validate project and user info using keystone
    auth = v3.Password(user_domain_name='default', username='admin',password='Nexii123',project_domain_name='default', project_name='admin', auth_url='http://localhost:5000/v3')
    sess = session.Session(auth=auth)
    keystone = client.Client(session=sess)
    d = keystone.domains.list()
  #check if project exists
    try:
        pf= keystone.projects.find(name=prj)
        if pf:
            projtouse = pf
        else:
            projtouse = keystone.projects.create(prj, d[0])
            print "New Project created"
    except:
        projtouse = keystone.projects.create(prj, d[0])
        print "New project created"
       #check for users
    try:
        uf = keystone.users.find(name=usr, project=projtouse)
        if uf:
            usertouse = uf
    except:
        usertouse  = keystone.users.create(name=usr, password=passwd, project=projtouse, domain=d[0])
        access=role
        access_role(usertouse,projtouse,access,keystone)

       #Use the values given by user after validation
    projectname=projtouse.to_dict()['name']
    username=usertouse.to_dict()['name']

def attachtovm(username,volid,nova):
    iso=[x.id for x in nova.images.list()]
    flavors=[ x.id for x in nova.flavors.list()]
    print nova.servers.create(username,iso[0],flavors[0])
    print "Please wait building vm..."
    import time; time.sleep(120)
    print "Attaching volume..."
    nova.volumes.create_server_volume(nova.servers.find().id,volid)
    import time; time.sleep(120)
    print "volume attached to VM"

def cinder_ops(projectname,username,password,role,vol_axn,vol_typ, vol_siz, vol_to_attch, vol_to_del):
    auth1 = v3.Password(user_domain_name='default', username=username,password=password,project_domain_name='default', project_name=projectname, auth_url='http://controller:5000/v3')
    sess1 = session.Session(auth=auth1)
    cin = ciclient.Client('2.0',session=sess1)
    val = vol_axn.split(',')
    for v in val:
        if v == "create":
            print "Creating Volume:"
            voltp=vol_typ
            volnm=username+projectname+voltp
            sz=vol_siz
            myvol=cin.volumes.create(name=volnm,size=sz,volume_type=voltp)
            print "Volume created successfully with volume id: \n"+myvol.id
        elif v=="list":
            print "List Volumes:"
            import time; time.sleep(40)
            vols = cin.volumes.list()
            if not vols:
                print "No volumes are present in this project"
            else:
                for i in vols:
                    print i
                    print "size : ",i.to_dict()['size']
                    print "name : ",i.to_dict()['name']
                    print "status : ",i.to_dict()['status']
                    print "volume_type : ", i.to_dict()['volume_type']
                    print "\n"
        elif v=="attach":
            vn = cin.volumes.find(name=vol_to_attch)
            vid = vn.to_dict()['id']
            nova=nova_c.Client('2.0', session=sess1)
            attachtovm(username,vid,nova)
        elif v=="delete":
            print "Deleting Volume:"
            import time; time.sleep(40)
            vn = cin.volumes.find(name=volnm)
            vid = vn.to_dict()['id']
            cin.volumes.delete(vid)
            print "Volume "+volnm+" has been deleted successfully"

def get_input():
    f = open('vars.yml')
    for line in f:
        try:
            line = line.strip().split(':')
            key = line[0].strip()
            val = line[1].strip()
            if key=='username':
                usr=val
                print "User:"+usr
            if key=='projectname':
                prj=val
                print "Project:"+prj
            if key=='password':
                psswd=val
            if key=='role':
                role=val
                print "Role:"+role
            if key=='volume_action':
                vol_axn=val
            if key=='volume_type':
                vol_typ=val
            if key=='volume_size':
                vol_siz=val
            if key=='volume_to_attach':
                vol_attch=val
            if key=='volume_to_delete':
                vol_del=val
        except IndexError:
            pass
    validate_as_admin(usr,prj,psswd, role)
    cinder_ops(prj, usr, psswd,role,vol_axn,vol_typ, vol_siz, vol_attch, vol_del)


def main():
     get_input()

if __name__=="__main__":main()



                                                                                                     
