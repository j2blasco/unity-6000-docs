* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetPort.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).GetPort
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public static int GetPort(); 
### Returns
**int** The port number of the ChannelService. 
### Description
Retrieves the port where the ChannelService runs. This port is chosen randomly when the ChannelService first starts. Alternatively you can specify the port from the command line, using the --ump-channel-service-port <portNumber> switch.
* * *
