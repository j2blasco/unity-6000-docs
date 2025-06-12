* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes-needsRetetrahedralization.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).needsRetetrahedralization
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
An event which is called when the number of currently loaded light probes changes due to additive scene loading or unloading.
For GameObjects rendered using light probe data, Unity uses a tetrahedral space mapping to calculate which light probes to use when rendering each GameObject based on the object's position.  
  
When new light probe data is added or existing light probe data is removed, the tetrahedral space mapping between the light probe positions needs to be re-calculated to account for the new light probes which have been additively loaded in, or for the removed probes which belonged to a scene that was unloaded.  
  
This `needsRetetrahedralization` event is triggered when you either additively load or unload Scenes which contain light probe data, allowing you to decide when you should make the call to [LightProbes.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html) or [LightProbes.TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html) to retetrahedralize the light probe data.  
  
Because light probe data is considered to be external data that is referenced in the scene, but is not part of the scene itself, it is asynchronously loaded and can sometimes load in after the scene load/unload operation appears to have completed.  
  
Therefore if you are loading or unloading scenes which contain light probe data, you should use this event to determine when to retetrahedralize, rather than relying on the [SceneManager.sceneLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager-sceneLoaded.html) event, because when the sceneLoaded event is called, the new light probe data may not yet be up-to-date.  
  
In addition, if you are loading multiple scenes which each contain additional light probe data, you should wait for the corresponding number of `needsRetetrahedralization` events before retetrahedralizing the light probe data, because recalculating it after each event would be time-consuming and unnecessary. For example, if you were to additively load five scenes which each contain light probe data, you should wait for all five needsRetetrahedralization events before calling [LightProbes.Tetrahedralize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.Tetrahedralize.html) or [LightProbes.TetrahedralizeAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.TetrahedralizeAsync.html).
* * *
