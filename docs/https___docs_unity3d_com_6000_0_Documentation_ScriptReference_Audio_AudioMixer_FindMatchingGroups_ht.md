* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.FindMatchingGroups.html

#  [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html).FindMatchingGroups
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
public AudioMixerGroup[] FindMatchingGroups(string subPath); 
### Parameters
Parameter | Description  
---|---  
subPath | Path sub-strings to match with.  
### Returns
**AudioMixerGroup[]** Groups in the mixer whose paths match the specified search path. 
### Description
Connected groups in the mixer form a path from the mixer's master group to the leaves. This path has the format **Master Group/Child of Master Group/Grandchild of Master Group** , and so on. For example, in the hierarchy below, the group DROPS has the path **Master/WATER/DROPS**. To return only the group called **DROPS** , enter **DROPS**. The substring **Master/AMBIENCE** returns three groups, **AMBIENCE/CROWD** , **AMBIENCE/ROAD** , and **AMBIENCE**. The substring **/R** would return both **ROAD** and **RIVER**.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/AudioMixerFindMatchingGroupsExampleHeirarchy.png)
```
using UnityEngine;
using UnityEngine.Audio;  
  
public class FindMatchingMixerGroups : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AudioMixer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html) mixer;  
  
    static void PrintGroups(AudioMixerGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixerGroup.html)[] groups)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("---- MIXER GROUPS ----");
        foreach (var group in groups)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(group);
        }
    }  
  
    void Start()
    {
        // Will find all groups with a path containing the substring "DROPS"
        // In the example, this is a single group defined by the path Master/WATER/DROPS.
        var groups = mixer.FindMatchingGroups("DROPS");
        PrintGroups(groups);  
  
        // Will find all groups with a path containing the substring "Master/AMBIENCE"
        // In the below example, this matches three groups "Master/AMBIENCE/CROWD", "Master/AMBIENCE/ROAD", and "Master/AMBIENCE".
        groups = mixer.FindMatchingGroups("Master/AMBIENCE");
        PrintGroups(groups);
    }
}

```

* * *
