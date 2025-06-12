* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetChannelClientList.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).GetChannelClientList
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
public static ChannelClientInfo[] GetChannelClientList(); 
### Returns
**ChannelClientInfo[]** A list that contains the ChannelInfo for every channel client. 
### Description
Gets a list of all channel clients connected to the [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).
This method lists all connections to the [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html), regardless of which channels they are connected to. For example, the "events" channel might have multiple [ChannelClient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html)s connected to it.
* * *
