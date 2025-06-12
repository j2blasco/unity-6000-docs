* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-isPartOfStaticBatch.html

#  [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html).isPartOfStaticBatch
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
isPartOfStaticBatch; 
### Description
Indicates whether the renderer is part of a [static batch](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html) with other renderers.
Unity sets this flag after it generates the static batch that contains the renderer. Be aware that Unity generates static batches at different times for the Unity Player and Unity Editor:  
  
* **Unity Player** : Unity generates static batches for renderers in every scene at build time. This means that `Renderer.isPartOfStaticBatch` is always valid in a built application. * **Unity Editor** : Unity builds static batches for renderers in a scene only after it loads the scene in Play mode. This means that `Renderer.isPartOfStaticBatch` is only valid in the Unity Editor while in Play mode after Unity loads the scene that the renderer is in.  
  

* * *
