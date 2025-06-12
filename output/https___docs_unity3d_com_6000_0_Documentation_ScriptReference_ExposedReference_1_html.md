* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedReference_1.html

# ExposedReference<T0>
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Creates a type whos value is resolvable at runtime.
ExposedReference is a generic type that can be used to create references to Scene objects and resolve their actual values at runtime and by using a context object. This can be used by assets, such as a [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) or [PlayableAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.html) to create references to Scene objects.  
  
The example below shows how a [PlayableAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.html) can use exposed references to create references to a Scene GameObject. This is an example that uses Timeline, so you may want to [set up your GameObject in Timeline](https://docs.unity3d.com/Packages/com.unity.timeline@latest/index.html?subfolder=/manual/wf-create-instance.html) and [make an animation with your GameObject](https://docs.unity3d.com/Packages/com.unity.timeline@latest/index.html?subfolder=/manual/wf-record-anim.html).
```
//Put both of these scripts in your Project, then go to your Timeline, click the **Add** dropdown and choose **Playable Track**. Place this script on your Timeline as a Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) Track
//Click on the track and choose a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) from your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) in the "My Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Object" field. Also set the velocity.  
  
using UnityEngine;
using UnityEngine.Playables;  
  
[System.Serializable]
public class ExposedReferenceExample : PlayableAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.html)
{
    //This allows you to use GameObjects in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
    public ExposedReference<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> m_MySceneObject;
    //This variable allows you to decide the velocity of your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_SceneObjectVelocity;  
  
    public  override Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) CreatePlayable(PlayableGraph[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) graph , GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) myGameObject)
    {
        //Get access to the Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) Behaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html) script
        TestExample playableBehaviour = new TestExample();
        //Resolve the exposed reference on the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) by returning the table used by the graph
        playableBehaviour.m_MySceneObject = m_MySceneObject.Resolve(graph.GetResolver());  
  
        //Make the PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html) velocity variable the same as the variable you set
        playableBehaviour.m_SceneObjectVelocity = m_SceneObjectVelocity;  
  
        //Create a custom playable from this script using the Player Behaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html) script
        return ScriptPlayable<TestExample>.Create(graph, playableBehaviour);
    }
}

```

Place this next script in your Project in the same folder as the above script. This script changes the behaviour of the timeline by moving the Scene GameObject while the Playable Track is playing.
```
using  UnityEngine;
using  UnityEngine.Playables;  
  
public  class TestExample : PlayableBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_MySceneObject;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_SceneObjectVelocity;  
  
    public override void PrepareFrame(Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) playable, FrameData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) frameData)
    {
        //If the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exists, move it continuously until the Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) pauses
        if (m_MySceneObject != null)
            //Move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) using the velocity you set in your Playable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) Track's inspector
            m_MySceneObject.transform.Translate(m_SceneObjectVelocity);
    }
}

```

### Properties
Property | Description  
---|---  
[defaultValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedReference_1-defaultValue.html) | The default value, in case the value cannot be resolved.  
[exposedName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedReference_1-exposedName.html) | The name of the ExposedReference.  
### Public Methods
Method | Description  
---|---  
[Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedReference_1.Resolve.html) | Gets the value of the reference by resolving it given the ExposedPropertyResolver context object.  
* * *
