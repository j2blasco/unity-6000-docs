* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MinMaxSlider.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).MinMaxSlider
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
**Obsolete** Switch the order of the first two parameters.
## Declaration
public static void MinMaxSlider([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, ref float minValue, ref float maxValue, float minLimit, float maxLimit); 
## Declaration
public static void MinMaxSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, ref float minValue, ref float maxValue, float minLimit, float maxLimit); 
## Declaration
public static void MinMaxSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, ref float minValue, ref float maxValue, float minLimit, float maxLimit); 
## Declaration
public static void MinMaxSlider([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, ref float minValue, ref float maxValue, float minLimit, float maxLimit); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the slider.  
label | Optional label in front of the slider.  
minValue | The lower value of the range the slider shows, passed by reference.  
maxValue | The upper value at the range the slider shows, passed by reference.  
minLimit | The limit at the left end of the slider.  
maxLimit | The limit at the right end of the slider.  
### Description
Makes a special slider the user can use to specify a range between a min and a max.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIMinMaxSlider.png)   
_MinMax Slider in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Place the selected object randomly between the interval of the Min Max Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)
// in the X,Y,Z coords  
  
class EditorGUIMinMaxSlider : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    float minVal = -10;
    float minLimit = -20;
    float maxVal = 10;
    float maxLimit = 20;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Move Object Randomly")]
    static void Init()
    {
        var window = GetWindow<EditorGUIMinMaxSlider>();
        window.Show();
    }  
  
    void OnGUI()
    {
        EditorGUI.MinMaxSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MinMaxSlider.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, position.width, 20),
            new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Random[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html) range:"),
            ref minVal, ref maxVal,
            minLimit, maxLimit);
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 25, position.width, position.height - 25), "Randomize!"))
        {
            PlaceRandomly();
        }
    }  
  
    void PlaceRandomly()
    {
        if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            Selection.activeTransform.position =
                new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(
                    Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(minVal, maxVal),
                    Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(minVal, maxVal),
                    Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(minVal, maxVal)
                );
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Select a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to randomize its position.");
        }
    }
}

```

* * *
