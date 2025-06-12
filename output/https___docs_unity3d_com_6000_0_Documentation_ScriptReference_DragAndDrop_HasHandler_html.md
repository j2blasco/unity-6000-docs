* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.HasHandler.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).HasHandler
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
public static bool HasHandler(int dropDstId, Delegate handler); 
### Parameters
Parameter | Description  
---|---  
dropDstId | ID of the destination window.  
handler | The handler of the targeted window.  
### Returns
**bool** True if the handler is already registered. 
### Description
Check if the handler is already registered for the destination window ID.
* * *
