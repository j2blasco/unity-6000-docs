* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html

# AnimationMode
class in UnityEditor
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
[AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) is used by the [AnimationWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationWindow.html) to store properties modified by the [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) playback.
When exiting [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) all properties are reverted to their default state. Animated properties are also highlighted by the inspector. Use [StartAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StartAnimationMode.html) to enter Animation mode. In Animation mode the editor is tinted to show that it is animating. Properties can be animated via [SampleAnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html).  
  
The following script example shows how a GameObject can be animated. [AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) has functions which support this. The demo can be launched from the "Examples/AnimationMode demo" menu. Once this demo starts it requires a GameObject to be selected in the Scene window. (This example requires the game to not be running in the Game view.) After a GameObject has been selected the example window will change. Choose a created animation clip for the chosen GameObject. Once the animation clip has been loaded the animation can be applied to the GameObject. Clicking the Animate button adds a slider to the window. Using the slider will apply the animation to the selected GameObject. The Lock button prevents the animation to be applied to a different GameObject. 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    protected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go;
    protected AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) animationClip;
    protected float time = 0.0f;
    protected bool lockSelection = false;
    protected bool animationMode = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/AnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) demo", false, 2000)]
    public static void DoWindow()
    {
        var window = GetWindowWithRect<ExampleClass>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 300, 80));
        window.Show();
    }  
  
    // Has a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) been selection?
    public void OnSelectionChange()
    {
        if (!lockSelection)
        {
            go = Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html);
            Repaint();
        }
    }  
  
    // Main editor window
    public void OnGUI()
    {
        // Wait for user to select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        if (go == null)
        {
            EditorGUILayout.HelpBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HelpBox.html)("Please select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)", MessageType.Info[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.Info.html));
            return;
        }  
  
        // Animate and Lock buttons.  Check if Animate has changed
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(AnimationMode.InAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html)(), "Animate");
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
            ToggleAnimationMode();  
  
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        lockSelection = GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(lockSelection, "Lock");
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();  
  
        // Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) to use when Animate has been ticked
        EditorGUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html)();
        animationClip = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(animationClip, typeof(AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)), false) as AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html);
        if (animationClip != null)
        {
            float startTime = 0.0f;
            float stopTime  = animationClip.length;
            time = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)(time, startTime, stopTime);
        }
        else if (AnimationMode.InAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html)())
            AnimationMode.StopAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StopAnimationMode.html)();
        EditorGUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html)();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (go == null)
            return;  
  
        if (animationClip == null)
            return;  
  
        // Animate the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        if (!EditorApplication.isPlaying[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlaying.html) && AnimationMode.InAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html)())
        {
            AnimationMode.BeginSampling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.BeginSampling.html)();
            AnimationMode.SampleAnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html)(go, animationClip, time);
            AnimationMode.EndSampling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.EndSampling.html)();  
  
            SceneView.RepaintAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RepaintAll.html)();
        }
    }  
  
    void ToggleAnimationMode()
    {
        if (AnimationMode.InAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html)())
            AnimationMode.StopAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StopAnimationMode.html)();
        else
            AnimationMode.StartAnimationMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StartAnimationMode.html)();
    }
}

```

### Static Properties
Property | Description  
---|---  
[animatedPropertyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode-animatedPropertyColor.html) | The color used to show that a property is currently being animated.  
[candidatePropertyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode-candidatePropertyColor.html) | The color used to show that an animated property has been modified.  
[recordedPropertyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode-recordedPropertyColor.html) | The color used to show that an animated property automatically records changes in the animation clip.  
### Static Methods
Method | Description  
---|---  
[AddEditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.AddEditorCurveBinding.html) | Marks a property defined by an EditorCurveBinding as currently being animated.  
[AddPropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.AddPropertyModification.html) | Marks a property as currently being animated.  
[BeginSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.BeginSampling.html) | Initialise the start of the animation clip sampling.  
[EndSampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.EndSampling.html) | Finish the sampling of the animation clip.  
[InAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.InAnimationMode.html) | Checks whether the Editor is in Animation mode.  
[IsPropertyAnimated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.IsPropertyAnimated.html) | Checks whether the specified property is in Animation mode and is being animated.  
[SampleAnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SampleAnimationClip.html) | Samples the AnimationClip for the GameObject and also records modified properties when in Animation mode.  
[SamplePlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.SamplePlayableGraph.html) | Samples the specified output index of a PlayableGraph and also records modified properties when in Animation mode.  
[StartAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StartAnimationMode.html) | Starts the Animation mode.  
[StopAnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.StopAnimationMode.html) | Stops the Animation mode and reverts any properties that were animated while in Animation mode.  
* * *
