 # Aiven-Kafka-Python-Quickstart
## A simple tutorial to get started using Kafka services managed by Aiven 
Aiven (pronounced ai-vn) makes it convenient to quickly experiment with many types of datastores.
Today we're going to be taking a look at how to quickly setup an Aiven account, create a kafka service with observability and monitoring through Graphana, and demonstrate it's use by emulating an IoT device that publishes simple weather data to Kafka.

## Prerequisites
This tutorial assumes you have python installed and correctly and correctly and correctly and correctly and correctly and correctly and correctly and correctly configured on your system.
You will need to ensure that you have the kafka-python and timezone packages installed. This can be accomplished using pip.
``` 
 pip install kafka-python 
 ```
``` 
 pip install timezone
 ```
You'll also need to set up a total of three services on the Aiven platform, the kafka service itself, InfluxDB where kafka will send its' metric data, and graphana, which will provide observabilty. Aiven provides a free one month trial with $300 in credit for all new accounts which is more than enough for our needs. This [link](https://console.aiven.io/signup/email) takes you to the signup page. The instructions are very easy to follow.  I recommend setting up a username and password rather than a third party service like Google to create your account for simplicty. The platform provides a very simple guide that walks you through some of the features of the account and provides some limited tailoring of the information it presents if you answer some of their questions.  The services are as easy to tear down as they are to set up so remember that if you need to you can always delete a service and recreate it.

Once you've created your account we can set up the services.

## Kafka
First we'll set up a kafka service. Find and click on the Service link at the top of the left navigation bar.
<img align="left" width="100" height="200" src=Navigation-panel.png />
From here we want to click on the Create a new service button.
From here, click on the kafka image to select service, select the cloud provider that you want to host kafka (I chose GCP but it really doesn't matter for our purposes), select the appropriate region for your cloud provider, and finally select the service plan (I suggest the smallest "Startup" plan). Now just click create and wait for the magic to happen. It will take a few minutes for Aiven to complete the provisioning and configuration.

## InfluxDB
We will be using InfluxDB as the storage place for our Kafka metrics.  The process for setting up InfluxDB is similar to that of setting up a Kafka service but instead of selecting the Kafka service icon you will select the InfluxDB service icon. Select the same cloud provider, cloud provider region, and Startup service plan, then click create.

## Graphana
We will be using Graphana as our monitoring tool for the Kafka service. It will read the monitoring data from the InfluxDB service.  Repeat the steps to create the previous 2 services but select the Graphana service icon instead of Kafka or InfluxDB.

## Service integration
Once all three services have completed deployment (there will be nothing but green circles in the "nodes" column of the services dashboard) click on the row containing InfluxDB. This will take you to the Overview page for the selected service. This page contains the configuration information for the service. Locate the "Service Integbrations" section and click on the "Manage Integrations" button. This brings up a selection of intefrations available to the InfluxDB service. find the "Metrics" icon on the lower left of the popup and click the "User integration" button. The drop-down box that appears will be pre-populated with available services. Select the Kafka service from the drop-down and click "Enable". When this is completed, repeat the steps again to create the Graphana integration. And that's it for integration work!

## Validating Observability
Go to the service overview tab for Graphana and note the service URI, username, and password.  Open a browser tab with the address in the Service URI and log into your Graphana service with the username and password. Once you're logged into Graphan, select "Browse" from the dashboard navigation menu on the left navigation pane. There you will find a pre-configured dashboard. Clicking on the resource will take you to it. We can now see lots of pretty charts but are we certain that it's actually hooked up? Let's do that by submitting events to Kafka and observe the impact on the dashboard.

## Submitting events to Kafka
The simple demo program will emulate an IoT device taking some simple weather data, say an app on a users phone which crowdsources weather data for creating precise weater locally.
In order to submit the events, we will need to be able to communicate with Kafka.  Go the the service overview for your Kafka service.  You'll want to copy the service URI, and download the Access Key, Access Certificate, and the CA Certificate. These will need to be passed as parameters the python script. In addition, we will need a topic to receive the events that we publish. To create the topic, click on the "Topics" tab to the right of the Overview tab.Add a new topic called "sensor-data" into the text box and click "Add topic". Once the topic has been created you can click on the topic name to create a pop-up that presents detailed topic info for more details.

Invoke the script using the command below being sure to replace the dummy data with the data you got from the service overview information. The message-count parameter is how many events will be sent to Kafka. Given the speed of the services and the size of our payload, you'll want to set the message-count to at least 100k in order to easliy see the impact on the dashboard.
```
./main.py --service-uri kafka-service-uri.aivencloud.com:11884 --ca-path path/to/ca.pem --key-path path/to/service.key --cert-path path/to/service.cert --message-count 200000
```
Once you start sending events you can watch the dashboard as the resource usage spikes under the load.
If you want to easily look at the messages that the topic has received we can do that as well. Go to the Service overview tab of the Kafka service and locate the "Apache Kafka REST API" toggle switch and enable it. Then go back to the topic info pop-up as described above and click ont the "Messages" button. After landing on the messages page, click the "Fetch Messages" button.  The response may not look like what you expect.  Where did the JSON go? By default, the filter is set to return messages in a binary format. To see the actual JSON without having to fetch the messages again, you can simply click the toggle labelled "Decode from base64", and you can now examine the messages in JSON format.

## Conclusion
This is all that's needed to set up a Kafka service, export metrics, and be able to observe the metrics from a dashboard!
