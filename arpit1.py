import os
print("\t\t--------------Hello World-------------------")
print()
print('''
        \tPress 1 : Date command
       
        \t\t HADOOP
    
        \tPress 2 : Start hadoop namenode service
        \tpress 3 : Stop hadoop namenode service
        \tPress 4 : Start hadoop datanode service
        \tpress 5 : Stop hadoop datanode service
        \tPress 6 : Check hadoop cluster report
        \tPress 7 : To checks files on hadoop cluster 
       
        \t\t Docker
        
        \tPress 8 : To start the Docker Service
        \tPress 9 : To download docker image
        \tPress 10 : To list all the containers
        \tPress 11 : To list running containers
        \tPress 12 : To Launch the Container
        \tPress 13 : To start the container
        \tPress 14 : To attach the container to the terminal
        \tPress 15 : To delete a container
        \tPress 16 : To delete all the containers
        
	\t\t AWS-CLI

	\tPress 17 : To login to the AWS-CLI
	\tPress 18 : To see all the instances 
	\tPress 19 : To see all the key pairs
	\tPress 20 : To see Security groups
	\tPress 21 : To Create key Pairs
	\tPress 22 : To Create Security Groups
	\tPress 23 : To Create volume
	\tPress 24 : Attach Volume
	\tPress 25 : Launch an instance with keypair and security group
	\tPress 26 : Create S3 Bucket
	\tPress 27 : To upload static data on your Bucket and making it public
	\tPress 28 : Start an Instance
	\tPress 29 : Stop an Instance
	\tPress 30 : Terminate Instance
	\tPress 31 : EXIT
''')
print()
while True:
    print()
    choice= int(input("Enter your choice : "))
    print()
    if choice==1:
        os.system("date")

    elif choice==2:
        os.system("hadoop-daemon.sh start namenode")
   
    elif choice==3:
        os.system("hadoop-daemon.sh stop namenode")
   
    elif choice==4:
        os.system("hadoop-daemon.sh start datanode")

    elif choice==5:
        os.system("hadopp-daemon.sh stop datanode")
    
    elif choice==6:
        os.system("hadoop dfsadmin -report")

    elif choice==7:
        os.system("hadoop fs -ls")

    elif choice==8:
        os.system("systemctl start docker")

    elif choice==9:
        p=input("Enter the OS with version to be downloaded : ")
        os.system("docker pull {}".format(p))

    elif choice==10:
        os.system("docker ps -a")

    elif choice==11:
        os.system("docker ps")
                
    elif choice==12:
        p=input("Enter OS to be launched : ")
        os.system("docker run -it {}".format(p))

    elif choice==13:
        name=input("Enter the name of OS to be started : ")
        os.system("docker start {}".format(name))

    elif choice==14:
        n=input("Enter the name of terminal to be attached : ")
        os.system("docker attach {}".format(n))

    elif choice==15:
        n=input("Enter the name of the container to be deleted : ")
        os.system("docker rm {}".format(n))
    
    elif choice==16:
        os.system("docker rm `docker ps -a -q`")

    elif choice==17:
        os.system("aws configure")
 
    elif choice==18:
        os.system("aws ec2 describe-instances")

    elif choice==19:
        os.system("aws ec2 describe-key-pairs")

    elif choice==20:
        os.system("aws ec2 describe-security-groups")

    elif choice==21:
        key = input("Enter the name of Key you want to create : ")
        os.system("aws ec2 create-key-pair --key-name {}".formate(key))

    elif choice==22:
        name = input("Enter the name of security group you want to create : ")
        description = input("Enter the description for your security group : ")
        os.system("aws ec2 create-security-group --group-name {} --description {}".format(name,description))

    elif choice==23:
        size = input("Enter the size of volume to be created in GB : ")
        zone = input("Enter the avaibility zone : ")
        os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {}".format(size,zone))

    elif choice==24:
        volume = input("Enter the id of volume : ")
        instance = input("Enter the id of instance in which volume has to be attached : ")
        device = input("Enter the name of volume eg.= /dev/sdf : ")
        os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".formate(volume,instance,device))

    elif choice==25:
        image = input("Enter ID of image : ")
        t = input("Enter the type of instance you want to run : ")
        sg = input("Enter the ID of security group you want to attach : ")
        key = input("Enter the name of existing key-pairs you want to attach : ")
        os.system("aws ec2 run-instances --image-id {} --instance-type {} --security-group-ids {} --key-name {}".format(image,t,sg,key))


    elif choice==26:
        name = input("Enter the Unique name for your bucket : ")
        region = input("Enter the name of region in which bucket has to be created : ")
        os.system("aws s3 mb s3://{} --region {}".format(name,region))

    elif choice==27:
        location = input("Enter the location of your static file : ")
        name = input("Enter the name of file : ")
        bucket = input("Enter the name of the bucket in which file has to be stored")
        os.system("aws s3 {}/{} s3://{}/{} --acl public-read".format(location,name,bucket,name))

    elif choice==28:
        name = input("Enter the ID of instance : ")
        os.system("aws ec2 start-instances --instance-ids {}".format(name))

    elif choice==29:
        name = input("Enter the ID of the instance : ")
        os.system("aws ec2 stop-instances --instance-ids {}".format(name))

    elif choice==30:
        name = input("Enter the ID of the instance : ")
        os.system("aws ec2 terminate-instances --instance-ids {}".format(name))

    elif choice==31:
        break
