* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClientScope-ctor.html

# ChannelClientScope Constructor
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
public ChannelClientScope(bool autoTick, string channelName, Action<string> handler, bool closeClientOnExit); 
## Declaration
public ChannelClientScope(bool autoTick, string channelName, Action<byte[]> handler, bool closeClientOnExit); 
### Parameters
Parameter | Description  
---|---  
autoTick | If true, starts the channel client in auto tick mode.  
channelName | Name of the channel to open.  
handler | Handler to process message on the channel.  
closeClientOnExit | If true, closes the client on exit.  
### Description
Create a new Channel Client scope.
* * *
