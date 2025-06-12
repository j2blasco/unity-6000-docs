* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Send.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).Send
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
public static void Send(int connectionId, byte[] data); 
## Declaration
public static void Send(int connectionId, string data); 
### Parameters
Parameter | Description  
---|---  
connectionId | The connection ID. This matches ChannelClientInfo.channelClientId.  
data | Data to send to the connected client.  
### Description
Sends a message to a specific connection. The message can be binary or UTF8.
* * *
