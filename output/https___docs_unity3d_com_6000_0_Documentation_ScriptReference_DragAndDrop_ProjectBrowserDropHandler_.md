* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.ProjectBrowserDropHandler.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).ProjectBrowserDropHandler
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
public delegate [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) ProjectBrowserDropHandler(int dragInstanceId, string dropUponPath, bool perform); 
### Parameters
Parameter | Description  
---|---  
dragInstanceId | ID of the dragged asset that is dropped into the Project browser window.  
dropUponPath | Path of the dragged asset that is dropped into the Project browser window.  
perform | True if the event is of type EventType.DragPerform.  
### Returns
**DragAndDropVisualMode** Returns [DragAndDropVisualMode.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.None.html) if this handler is not able to process the event. In that case a new handler will be called for processing. Any other [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) results will stop the handler chain. 
### Description
Handler for the Project.
* * *
