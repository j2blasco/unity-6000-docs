* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.BroadcastBinary.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).BroadcastBinary
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
public static void BroadcastBinary(int channelId, byte[] data); 
### Parameters
Parameter | Description  
---|---  
channelId | The ID of the channel to send the message to.  
data | The binary data to send.  
### Description
Sends a message to all of a specific channel's [ChannelClient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html) connections.
* * *
