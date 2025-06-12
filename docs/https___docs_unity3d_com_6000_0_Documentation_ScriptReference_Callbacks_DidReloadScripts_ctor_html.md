* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.DidReloadScripts-ctor.html

# DidReloadScripts Constructor
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
public DidReloadScripts(); 
## Declaration
public DidReloadScripts(int callbackOrder); 
### Parameters
Parameter | Description  
---|---  
callbackOrder | Order in which separate attributes will be processed.  
### Description
DidReloadScripts attribute.
The `callbackOrder` parameter determines the order in which the DidReloadScripts notifications will occur. Lower numbers will report earlier than higher numbers and Unity's internal processing has an order value of zero.
* * *
