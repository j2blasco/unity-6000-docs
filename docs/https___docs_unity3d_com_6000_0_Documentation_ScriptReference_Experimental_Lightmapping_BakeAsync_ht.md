* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.BakeAsync.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.html).BakeAsync
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
public static bool BakeAsync([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) targetScene); 
### Parameters
Parameter | Description  
---|---  
targetScene | The Scene to generate lighting data for.  
### Returns
**bool** Returns true if Unity successfully starts the lighting bake job. Returns false if Unity does not successfully start the lighting bake job. 
### Description
Starts an asynchronous lighting bake job for the target Scene.
Unity generates lighting data for the target Scene only, but Lights, Renderers, Terrains and emissive Materials from all open Scenes contribute to the lighting. Note that Renderers and Terrains contribute to the lighting only if their [StaticEditorFlags.ContributeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html) flag is enabled.  
  
Unity calls [bakeStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeStarted.html) when it starts the bake, and [bakeCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-bakeCompleted.html) when it completes the bake. You can monitor the progress of the bake using the [isRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping-isRunning.html) property. If Unity cannot start the bake, it prints a warning to the console.  
  
Note that Unity only performs the bake if Lightmapping.giWorkflowMode is set to [Lightmapping.GIWorkflowMode.OnDemand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.GIWorkflowMode.OnDemand.html). If this is not the case, this function immediately returns false.  
  
For synchronous bakes see [Bake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.Bake.html).  
  
Additional resources: [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).
* * *
