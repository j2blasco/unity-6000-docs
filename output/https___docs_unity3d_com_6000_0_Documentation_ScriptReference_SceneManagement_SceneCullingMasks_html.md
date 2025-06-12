* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.html

# SceneCullingMasks
class in UnityEditor.SceneManagement
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
Masks that control what kind of Scene views and Game views Unity should render a GameObject in.
You can set masks on Scenes via [EditorSceneManager.SetSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SetSceneCullingMask.html) and on render batches via [BatchRendererGroup.AddBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.AddBatch.html).
### Static Properties
Property | Description  
---|---  
[DefaultSceneCullingMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.DefaultSceneCullingMask.html) | Specifies the default culling mask for a Scene. Use the bits from this Scene culling mask for objects that you want to render in both in the Game view and the Scene view.  
[GameViewObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.GameViewObjects.html) | The bits from this mask specify GameObjects that Unity should render in Game view.  
[MainStageSceneViewObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.MainStageSceneViewObjects.html) | The bits from this mask specify GameObjects that Unity should render in Scene views showing the main stage.  
* * *
