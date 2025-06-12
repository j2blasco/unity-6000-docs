* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.GetAudioLanguage.html

#  [VideoClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html).GetAudioLanguage
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
public string GetAudioLanguage(ushort audioTrackIdx); 
### Parameters
Parameter | Description  
---|---  
audioTrackIdx | Index of the audio track you want to query in the video.  
### Returns
**string** The abbreviated name of the language. 
### Description
Gets the language of the video clip’s audio tracks, if the audio tracks have an assigned language.
This returns nothing if the track was created without a specified language. You can use this function to switch out audio tracks in your video depending on the language preference of the user. The audio language is normally a 2 or 3 letter language code following the ISO 639-2/T or 639-2/B standards. For example, the code for English is normally “en” or “eng”. Check your audio files to see what codes they have. Some audio tracks don't have language information, in which case this function returns an empty string.   
  
Additional resources: [VideoPlayer.EnableAudioTrack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EnableAudioTrack.html).
```
// This script loops through each of the audio tracks to check their languages. If their language matches your preferred language (userLanguage),
// this script enables that audio track and deactivates the other tracks. 
// You need to assign this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), and assign a VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) component to it in the Inspector. 
// Also set userLanguage to the language you want.   
  
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Video;  
  
public enum Language
{
    English, French, Spanish, German, Japanese, Chinese, Italian, Portuguese, Russian, Korean, Arabic, Danish, Dutch, Finnish, Icelandic
}  
  
public class GetAudioLanguageExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Dictionary to map user-friendly language names to shorthand codes. The codes for your files might be different. 
    public static readonly Dictionary<Language, string> LanguageCodes = new Dictionary<Language, string>
    {
        { Language.English, "eng" },
        { Language.French, "fra" },
        { Language.Spanish, "spa" },
        { Language.German, "deu" },
        { Language.Japanese, "jpn" },
        { Language.Chinese, "zho" },
        { Language.Italian, "ita" },
        { Language.Portuguese, "por" },
        { Language.Russian, "rus" },
        { Language.Korean, "kor" },
        { Language.Arabic, "ara" },
        { Language.Danish, "dan" },
        { Language.Dutch, "nld" },
        { Language.Finnish, "fin"},
        { Language.Icelandic, "isl"}
    };  
  
    VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html) videoPlayer;  
  
    // Choose your language. 
    public Language userLanguage;  
  
    void Start()
    {
        videoPlayer = GetComponent<VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)>();
        // Get the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) from the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)
        VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) clip = videoPlayer.clip;  
  
        if (clip != null)
        {
            // Get the number of audio tracks in the VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html)
            int audioTrackCount = clip.audioTrackCount;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("User chose " + userLanguage.ToString());  
  
            // Search the dictionary for the user's choice to get the language code. 
            if (LanguageCodes.TryGetValue(userLanguage, out string userLanguageCode))
            {
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("User language was " + userLanguage + " and the code is : " + userLanguageCode);
                // Loop through each audio track see if they have an assigned language that matches your language choice. 
                for (ushort i = 0; i < audioTrackCount; i++)
                {
                    string audioLanguage = clip.GetAudioLanguage(i);
                    Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Audio track " + i + " has language: " + audioLanguage);  
  
                    // If the audio track has the preferred language, enable this audio track. 
                    if (audioLanguage == userLanguageCode)
                    {
                        videoPlayer.EnableAudioTrack(i, true);
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Audio track " + i + " was enabled.");
                    }
                    // If the audio track doesn't have the chosen language, disable the track. 
                    else
                    {
                        videoPlayer.EnableAudioTrack(i, false);
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Audio track " + i + " was disabled.");
                    }
                }
            }
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No VideoClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoClip.html) assigned to the VideoPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).");
        }
    }
}
```

* * *
