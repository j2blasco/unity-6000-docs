* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.Combine.html

#  [StaticBatchingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.html).Combine
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
public static void Combine([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) staticBatchRoot); 
### Parameters
Parameter | Description  
---|---  
staticBatchRoot | The GameObject that should become the root of the combined batch.  
### Description
Combines all children GameObjects of the `staticBatchRoot` for static batching.
Static batching is a [draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) method that combines meshes that don't move to reduce [draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html). For more information about static batching, see [Static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html).  
  
This method copies the mesh data of the GameObjects into a single internal mesh. Each original GameObject is still present in the Scene which means Unity can still cull them individually.  
  
All child GameObjects under the `staticBatchRoot` must be eligible for static batching. For information on the eligibility requirements for static batching, see [Static batching at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching#runtime.html).  
  
After you combine the GameObjects, you can't change the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) properties of the children. However, you can change the Transform properties of the `staticBatchRoot`. Doing so transforms the entire combined batch.  
  
Note: You don't need to use this method with GameObjects you marked as Batching Static in the Editor. Unity prepares these GameObjects for static batching when it builds the Player.  
  
See also: [Mesh.CombineMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.CombineMeshes.html), [Mesh.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html).
* * *
## Declaration
public static void Combine(GameObject[] gos, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) staticBatchRoot); 
### Parameters
Parameter | Description  
---|---  
gos | The GameObjects to prepare for static batching.  
staticBatchRoot | The GameObject that should become the root of the combined batch.  
### Description
Combines all GameObjects in `gos` for static batching and treats `staticBatchRoot` as the root.
Static batching is a [draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) method that combines meshes that don't move to reduce [draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html). For more information about static batching, see [Static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html).  
  
This method copies the mesh data of the GameObjects into a single internal mesh. Each original GameObject is still present in the Scene which means Unity can still cull them individually.  
  
All GameObjects in `gos` must be eligible for static batching. For information on what a GameObject needs to be eligible for static batching, see [Static batching at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching#runtime.html).  
  
After you combine the GameObjects, you can't change the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) properties of the children. However, you can change the Transform properties of the `staticBatchRoot`. Doing so transforms the entire combined batch.  
  
Note: You don't need to use this API on GameObjects you marked as Batching Static in the Editor. Unity prepares these GameObjects for static batching when it builds the Player.  
  
  
  
See also: [Mesh.CombineMeshes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.CombineMeshes.html), [Mesh.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-isReadable.html).
* * *
