* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject-isConnected.html

#  [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html).isConnected
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
isConnected; 
### Description
Tests whether the [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html) is connected to an underlying version control system.
There are various reasons why your VersionControlObject may not be connected. For example: 
  * Your VCS might need to be configured before establishing connection.
  * [OnActivate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.OnActivate.html) might start a background thread that takes some time to connect.
  * The connection might get broken because of network issues.


In all these cases this property will return **false**.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
[VersionControl("Custom")]
public class CustomVersionControlObject : VersionControlObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html), ISettingsInspectorExtension[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ISettingsInspectorExtension.html)
{
    bool m_Active;
    bool m_IsConnected;  
  
    public override bool isConnected => m_IsConnected;  
  
    public void OnEnable()
    {
        // m_Active will be false if CustomVersionControlObject has just been activated.
        // It will be true if OnEnable was called after domain reload. In that case we want to reestablish connection.
        if (m_Active)
            Connect();
    }  
  
    public void OnDisable()
    {
        // Let's assume that domain reload kills connection to underlying VCS.
        Disconnect();
    }  
  
    public override void OnActivate()
    {
        m_Active = true;
        // Let's try to automatically establish connection to underlying VCS.
        // It will not work the first time CustomVersionControlObject is activated because username is not configured yet.
        // However it will work on subsequent Unity startup.
        Connect();
    }  
  
    public override void OnDeactivate()
    {
        m_Active = false;
        Disconnect();
    }  
  
    public void OnInspectorGUI()
    {
        var oldUsername = EditorUserSettings.GetConfigValue("vcCustomUsername");
        var newUsername = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("Username (hint: TestUser):", oldUsername);
        if (newUsername != oldUsername)
            EditorUserSettings.SetConfigValue("vcCustomUsername", newUsername);  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Connected:", m_IsConnected ? "Yes" : "No");  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Connect"))
            Connect();
    }  
  
    void Connect()
    {
        var username = EditorUserSettings.GetConfigValue("vcCustomUsername");
        m_IsConnected = username == "TestUser";
    }  
  
    void Disconnect()
    {
        m_IsConnected = false;
    }
}

```

Additional resources: [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html), [ISettingsInspectorExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ISettingsInspectorExtension.html).
* * *
