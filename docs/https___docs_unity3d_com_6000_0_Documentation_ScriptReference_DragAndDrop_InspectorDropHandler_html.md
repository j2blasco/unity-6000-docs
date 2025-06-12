* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.InspectorDropHandler.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).InspectorDropHandler
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
public delegate [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) InspectorDropHandler(Object[] targets, bool perform); 
### Parameters
Parameter | Description  
---|---  
targets | Target objects of the drag operation.  
perform | True if the event is of type [EventType.DragPerform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.DragPerform.html).  
### Returns
**DragAndDropVisualMode** Returns [DragAndDropVisualMode.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.None.html) if this handler is not able to process the event. In that case a new handler will be called for processing. Any other [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) results will stop the handler chain. 
### Description
Handler for the Inspector.
* * *
