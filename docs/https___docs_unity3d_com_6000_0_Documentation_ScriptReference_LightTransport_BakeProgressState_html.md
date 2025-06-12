* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.html

# BakeProgressState
class in UnityEngine.LightTransport
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
Interface for progress reporting.
This interface reports progress for an ongoing asynchronous bake operation and provides a method to request the cancellation of the operation.
### Constructors
Constructor | Description  
---|---  
[BakeProgressState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.Cancel.html) | Cancel the asynchronous operation.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.Dispose.html) | Dispose the BakeProgressState object.  
[IncrementCompletedWorkSteps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.IncrementCompletedWorkSteps.html) | Increments the amount of completed work steps for this progress state.  
[Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.Progress.html) | Get the progress value.  
[SetTotalWorkSteps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.SetTotalWorkSteps.html) | Sets the total amount of work steps for the progress state. Increase the completed work steps using BakeProgressState.IncrementCompletedWorkSteps.  
[WasCancelled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.WasCancelled.html) | Checks whether the work represented by this progress state was cancelled.  
* * *
