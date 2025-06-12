* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.UnregisterMessageHandler.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).UnregisterMessageHandler
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
public static void UnregisterMessageHandler(string channelName, Action<int,byte[]> handler); 
### Parameters
Parameter | Description  
---|---  
channelName | The channel to stop processing messages on.  
handler | The handler to unregister.  
### Description
Unregisters a specific handler from a Channel.
* * *
