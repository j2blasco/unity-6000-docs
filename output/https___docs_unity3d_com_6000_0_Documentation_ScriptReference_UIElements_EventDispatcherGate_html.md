* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcherGate.html

# EventDispatcherGate
struct in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
### Description
Gates control when the dispatcher processes events. 
Here is an example of using a gate:   
  
When the gate is instantiated, it closes automatically, causing the dispatcher to store the events it receives in a queue. At the end of the `using` block, Dispose is called, which triggers opening the gate. When all gates on a dispatcher open, the events stored in the queue are processed. Closing a gate while the event queue is processed does not stop it from being processed. Instead, a new queue is created to store new events.   
  
Here is an example of using a gate: 
```
 public class MyElement : VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
 {
     void Foo()
     {
         using (new EventDispatcherGate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcherGate.html)(dispatcher))
         {
             // do something that sends events
         }
     }
 }

```

### Constructors
Constructor | Description  
---|---  
[EventDispatcherGate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcherGate-ctor.html) |  Constructor.   
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcherGate.Dispose.html) |  Implementation of IDisposable.Dispose. Opens the gate. If all gates are open, events in the queue are processed.   
* * *
