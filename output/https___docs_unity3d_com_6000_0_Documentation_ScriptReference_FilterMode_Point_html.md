* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Point.html

#  [FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html).Point
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
Point filtering - texture pixels become blocky up close.
Additional resources: [Texture.filterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-filterMode.html), [texture assets](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html).
```
//This script changes the filter mode of your Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) you attach when you press the space key in Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html). It switches between Point, Bilinear and Trilinear filter modes.
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and attach a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to the My Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) field in the Inspector.
//Apply the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) to GameObjects (click and drag the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) onto a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) mode) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) to see it change modes in-game.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Remember to assign a Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) in the Inspector window to ensure this works
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) m_MyTexture;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space key to switch between Filter Modes
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)'s Filter Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)
            m_MyTexture.filterMode = SwitchFilterModes();
            //Output the current Filter Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html) to the console
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Filter mode : " + m_MyTexture.filterMode);
        }
    }  
  
    //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) between Filter Modes when the user clicks the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
    FilterMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) SwitchFilterModes()
    {
        //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) the Filter Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html) of the Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) when user clicks the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
        switch (m_MyTexture.filterMode)
        {
            //If the FilterMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) is currently Bilinear, switch it to Point on the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) click
            case FilterMode.Bilinear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Bilinear.html):
                m_MyTexture.filterMode = FilterMode.Point[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Point.html);
                break;  
  
            //If the FilterMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) is currently Point, switch it to Trilinear on the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) click
            case FilterMode.Point[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Point.html):
                m_MyTexture.filterMode = FilterMode.Trilinear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Trilinear.html);
                break;  
  
            //If the FilterMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) is currently Trilinear, switch it to Bilinear on the Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) click
            case FilterMode.Trilinear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Trilinear.html):
                m_MyTexture.filterMode = FilterMode.Bilinear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.Bilinear.html);
                break;
        }
        //Return the new Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) FilterMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html)
        return m_MyTexture.filterMode;
    }
}

```

* * *
