* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.IsPropertyAnimated.html

#  [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html).IsPropertyAnimated
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
public static bool IsPropertyAnimated([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target, string propertyPath); 
### Parameters
Parameter | Description  
---|---  
target | The object to determine if it contained the animation.  
propertyPath | The name of the animation to search for.  
### Returns
**bool** Whether the property search is found or not. 
### Description
Checks whether the specified property is in Animation mode and is being animated.
[IsPropertyAnimated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.IsPropertyAnimated.html) checks whether a property is being animated. This check requires also the object where the property can be found.  
  
`color` is searched for in the following script example . It is part of the `Renderer` object. Note that the example uses a sphere GameObject and an animation file, color.anim. The color animation in color.anim has the color varying from yellow to blue. 
```
// Demo showing how IsPropertyAnimated() can be used to determine if a property
// on an object is being animated. In this example the color in a Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) is
// animated.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    protected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go;
    protected AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) animationClip;
    protected float time = 0.0f;
    protected bool showColor = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/AnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) demo")]
    public static void DoWindow()
    {
        var window = GetWindow<ExampleClass>();
        window.Show();
    }  
  
    void OnGUI()
    {
        if (go == null)
        {
            EditorGUILayout.HelpBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HelpBox.html)("Select a GO", MessageType.Info[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.Info.html));
            return;
        }  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) slider");  
  
        if (animationClip == null)
        {
            AnimationMode.StartAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StartAnimationMode.html)();
            animationClip = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)>("Assets/color.anim");
        }  
  
        if (animationClip != null)
        {
            float startTime = 0.0f;
            float stopTime  = animationClip.length;
            time = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)(time, startTime, stopTime);
        }  
  
        if (showColor)
        {
            EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Red color being animated");
        }
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (go == null)
            return;  
  
        if (animationClip == null)
            return;  
  
        if (AnimationMode.InAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html)())
        {
            Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = go.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
            if (AnimationMode.IsPropertyAnimated[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.IsPropertyAnimated.html)(rend, "material._Color.r"))
            {
                showColor = true;
            }
            else
            {
                showColor = false;
            }  
  
            AnimationMode.BeginSampling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.BeginSampling.html)();
            AnimationMode.SampleAnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html)(go, animationClip, time);
            AnimationMode.EndSampling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.EndSampling.html)();  
  
            SceneView.RepaintAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RepaintAll.html)();
        }
    }  
  
    // Has a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) been selection?
    public void OnSelectionChange()
    {
        go = Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html);
        Repaint();
    }  
  
    public void OnDestroy()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Shutting down");
        AnimationMode.StopAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StopAnimationMode.html)();
    }
}

```

* * *
