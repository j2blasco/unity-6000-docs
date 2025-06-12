* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.SetCurve.html

#  [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html).SetCurve
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html "Go to AnimationClip Component in the Manual")
## Declaration
public void SetCurve(string relativePath, Type type, string propertyName, [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve); 
### Parameters
Parameter | Description  
---|---  
relativePath | Path to the game object this curve applies to. The `relativePath` is formatted similar to a pathname, e.g. "root/spine/leftArm". If `relativePath` is empty it refers to the game object the animation clip is attached to.  
type | The class type of the component that is animated.  
propertyName | The name or path to the property being animated.  
curve | The animation curve.  
### Description
Assigns the curve to animate a specific property.
If `curve` is null the curve will be removed. If a curve already exists for that property, it will be replaced.  
  
**Note:** `SetCurve` will only work at runtime for legacy animation clips. For non-legacy AnimationClips it is an editor-only function.  
  
The following script example shows how a `GameObject` position can be animated using an animation clip. An animated curve is set onto the [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) using `SetCurve()`. This example moves the x offset from 1.0 down to 0.0.  
  
The [SetCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.SetCurve.html) API can be used to animate a large variety of parameters. Some typical components such as [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) and [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) have easy to access variables. For example the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) has variables such as [Transform.localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localPosition.html). The x, y, and z values of the `localPosition` can be animated using the [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) API. View the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) documentation to see the variables and how they can be animated.  
  
The [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class also links to variables that can be animated. These come from the shader that is used for rendering. Using the "Edit Shader..." option from the material drop down shows all the parameters that can be animated. The material parameters are animated through the Renderer class that references them. All animatable material parameters start with the `material` prefix followed by the property name starting with an underscore. For example, color (`material._Color`) and scale (`material._BumpScale`) can be animated.  
  
The example script below shows how a GameObject can be animated in two ways at the same time. In this example, the position of the GameObject is animated, and the Material color is also changed over time.
```
// This script example shows how SetCurve() can be used
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Animate the position and color of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    public void Start()
    {
        Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim = GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();
        AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve;  
  
        // create a new AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)
        AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip = new AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)();
        clip.legacy = true;  
  
        // create a curve to move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and assign to the clip
        Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[] keys;
        keys = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)[3];
        keys[0] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(0.0f, 0.0f);
        keys[1] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(1.0f, 1.5f);
        keys[2] = new Keyframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html)(2.0f, 0.0f);
        curve = new AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html)(keys);
        clip.SetCurve("", typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)), "localPosition.x", curve);  
  
        // update the clip to a change the red color
        curve = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0.0f, 1.0f, 2.0f, 0.0f);
        clip.SetCurve("", typeof(Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)), "material._Color.r", curve);  
  
        // now animate the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        anim.AddClip(clip, clip.name);
        anim.Play(clip.name);
    }
}

```

Property names can be located by setting Asset Serialization to Force Text mode in the Editor settings. Use `Edit->Project Settings->Editor` to enable this mode. The text files that are then written by the editor will include the names of the properties. For example, the yaml file written for a Scene object will include the Camera settings. Looking at this yaml file will show:  
  
`m_BackGroundColor: {r: .192156866, g: .301960796, b: .474509805, a: .0196078438}`  
`m_NormalizedViewPortRect:`  
`  serializedVersion: 2`  
`  x: 0`  
`  y: 0`  
`  width: 1`  
`  height: 1`  
`near clip plane: .300000012`  
`far clip plane: 1000`  
`field of view: 60`  
`orthographic: 0`  
`orthographic size: 5`  
`m_Depth: -1`  
  
This shows that the name for the FOV parameter is "field of view". If you wanted to create an animation clip to animate the camera field of view, you would pass "field of view" as the propertyName.  
  
Another example is the access of `Light` settings. The `scene.unity` file (assuming a Scene called `scene`) will have a string for the light color. Script can access the light color by accessing `m_Color`. The Scene will need to have a light for this example to work.  
  
Additional resources: [ClearCurves](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.ClearCurves.html) function, and the [AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) class.
* * *
