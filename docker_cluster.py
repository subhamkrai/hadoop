#!/usr/bin/env python

import commands
import os
import time
size=raw_input("enter the cluster size")
id_hadoop=[]
ip_hadoop=[]
size=int(size)
for i in range(size):
	if i == 0:
		id_hadoop.append(commands.getoutput("docker run -itd --rm centos6:hadoopv1"))
		print commands.getstatusoutput("docker cp /home/leo/hadoop/conf_files_namenode/core-site.xml "+id_hadoop[i]+":/etc/hadoop/")	
		commands.getoutput("docker cp /home/leo/hadoop/conf_files_namenode/hdfs-site.xml "+id_hadoop[i]+":/etc/hadoop/")	
		print 'name node='+id_hadoop[i] 
	else:
                id_hadoop.append(commands.getoutput("docker run -itd --rm centos6:hadoopv1"))
		commands.getoutput("docker cp /home/leo/hadoop/conf_files_datanode/hdfs-site.xml "+id_hadoop[i]+":/etc/hadoop/")	
		commands.getoutput("docker cp /home/leo/hadoop/conf_files_datanode/core-site.xml "+id_hadoop[i]+":/etc/hadoop/")	
	ip_hadoop.append(commands.getstatusoutput(" docker exec "+id_hadoop[i]+" hostname -i"))


#print ip_hadoop
print i
status=commands.getstatusoutput(" docker exec "+id_hadoop[0]+" hadoop namenode -format")[0]
print status
time.sleep(5)

def start_hdfs(size):
        for i in range(size):
                if i == 0:
                        commands.getoutput(" docker exec "+id_hadoop[i]+" hadoop-daemon.sh start namenode ")
                else:
                        commands.getoutput(" docker exec "+id_hadoop[i]+" hadoop-daemon.sh start datanode")
        print "hdfs creation successful"



if status==0:
	start_hdfs(size)
