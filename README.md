
# Aiven-Kafka-Python-Quickstart
## A simple tutorial to get started using Kafka services managed by Aiven 
<p>
Aiven (pronounced ai-vn) makes it convenient to quickly experiment with many types of datastores.
Today we're going to be taking a look at how to quickly setup an Aiven account, create a kafka service with observability and monitoring through Graphana, and demonstrate it's use by emulating an IoT device that publishes simple weather data to Kafka.
</p>

## Prerequisites
<p> This tutorial assumes you have python installed and correctly and correctly and correctly and correctly and correctly and correctly and correctly and correctly configured on your system.<br>
You will need to ensure that you have teh kafka-python and timezone packages installed. This can be accomplished using pip.<br>
``` 
 pip install kafka-python 
 ```
 <br>
``` 
 pip install timezone
 ```
</p>
<p>
You'll also need to set up a total of three services on the Aiven platform, the kafka service itself, InfluxDB where kafka will send its' metric data, and graphana, which will provide observabilty. Aiven provides a free one month trial with $300 in credit for all new accounts which is more than enough for our needs. This ![link](https://console.aiven.io/signup/email) takes you to the signup page. The instructions are very easy to follow.  I recommend setting up a username and password rather than a third party service like Google to create your account for simplicty. The platform provides a very simple guide that walks you through some of the features of the account and provides some limited tailoring of the information it presents if you answer some of their questions.  The services are as easy to tear down as they are to set up so remember that if you need to you can always delete a service and recreate it</p>
<p>
Once you've created your account we can set up the services. First we'll set up a kafka service. Click on the Services link in the left hand navigation bar, as shown below.
![Navigation-panel](https://user-images.githubusercontent.com/1443943/172065100-ceb9f581-52be-4391-ae6a-dc55c9cf394d.png)
