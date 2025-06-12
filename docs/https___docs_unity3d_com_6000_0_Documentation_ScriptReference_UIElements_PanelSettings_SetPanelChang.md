* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.SetPanelChangeReceiver.html

#  [PanelSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.html).SetPanelChangeReceiver
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
public void SetPanelChangeReceiver([UIElements.IDebugPanelChangeReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDebugPanelChangeReceiver.html) value); 
### Description
Sets a custom IPanelChangeReceiver in the panelChangeReceiver setter to receive every change event. This method is available only in development builds and the editor, as it is a debug feature to go along the profiling of an application. 
Note that the values returned may change over time when the underlying architecture is modified.  
  
As this is called at every change marked on any visual element of the panel, the overhead is not negligible. The callback will not be called in release builds as the method is stripped.  
  
The following example uses the panelChangeReceiver in a game. To test it, add the component to a GameObject and the Panel Setting asset linked in the component fields.   
  

```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class ChangeLogger : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html), IDebugPanelChangeReceiver[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDebugPanelChangeReceiver.html)
{
    public PanelSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.html) panelSettings;
    public bool logChanges = true;
    public bool printOnConsole = false;
    public bool includeStacktrace = true;
    public List<ChangeEntry> changes;

    private void OnEnable()
    {
        panelSettings.SetPanelChangeReceiver(this);
    }

    public void Initialize()
    {
        changes.Clear();
    }

    public void OnVisualElementChange(VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) element, VersionChangeType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VersionChangeType.html) changeType)
    {
        if (logChanges)
        {

            if (changes == null)
                changes = new List<ChangeEntry>();

            changes.Add(new ChangeEntry()
            {
                changeType = changeType,
                element = element.ToString(),
                stackTrace = includeStacktrace ? Environment.StackTrace : null
            });
        }

        if (printOnConsole)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{string.Join(",", changeType.toStrings()),-40} {element}");
        }
    }

    [Serializable]
    public struct ChangeEntry
    {
        public string element;

        public VersionChangeType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VersionChangeType.html) changeType;

        [TextArea(10, 30)]
        public string stackTrace;
    }
}

public static class ChangeTypeHelpers
{
    public static List<string> toStrings(this VersionChangeType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VersionChangeType.html) type)
    {
        var changes = new List<string>();

        foreach (var value in (VersionChangeType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VersionChangeType.html)[])Enum.GetValues(typeof(VersionChangeType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VersionChangeType.html))))
        {
            if ((type & value) != 0)
                changes.Add(value.ToString());
        }
        return changes;
    }
}

```

* * *
