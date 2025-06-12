* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.html

# SystemLanguage
enumeration
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
The language the user's operating system is running in. Returned by Application.systemLanguage.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //This checks if your computer's operating system is in the French language
        if (Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) == SystemLanguage.French[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.French.html))
        {
            //Outputs into console that the system is French
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is in French. ");
        }
        //Otherwise, if the system is English, output the message in the console
        else if (Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html) == SystemLanguage.English[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.English.html))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("This system is in English. ");
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Afrikaans](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Afrikaans.html) | Afrikaans.  
[Arabic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Arabic.html) | Arabic.  
[Basque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Basque.html) | Basque.  
[Belarusian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Belarusian.html) | Belarusian.  
[Bulgarian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Bulgarian.html) | Bulgarian.  
[Catalan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Catalan.html) | Catalan.  
[Chinese](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Chinese.html) | Chinese.  
[Czech](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Czech.html) | Czech.  
[Danish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Danish.html) | Danish.  
[Dutch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Dutch.html) | Dutch.  
[English](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.English.html) | English.  
[Estonian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Estonian.html) | Estonian.  
[Faroese](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Faroese.html) | Faroese.  
[Finnish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Finnish.html) | Finnish.  
[French](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.French.html) | French.  
[German](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.German.html) | German.  
[Greek](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Greek.html) | Greek.  
[Hebrew](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Hebrew.html) | Hebrew.  
[Icelandic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Icelandic.html) | Icelandic.  
[Indonesian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Indonesian.html) | Indonesian.  
[Italian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Italian.html) | Italian.  
[Japanese](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Japanese.html) | Japanese.  
[Korean](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Korean.html) | Korean.  
[Latvian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Latvian.html) | Latvian.  
[Lithuanian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Lithuanian.html) | Lithuanian.  
[Norwegian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Norwegian.html) | Norwegian.  
[Polish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Polish.html) | Polish.  
[Portuguese](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Portuguese.html) | Portuguese.  
[Romanian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Romanian.html) | Romanian.  
[Russian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Russian.html) | Russian.  
[SerboCroatian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.SerboCroatian.html) | Serbo-Croatian.  
[Slovak](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Slovak.html) | Slovak.  
[Slovenian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Slovenian.html) | Slovenian.  
[Spanish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Spanish.html) | Spanish.  
[Swedish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Swedish.html) | Swedish.  
[Thai](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Thai.html) | Thai.  
[Turkish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Turkish.html) | Turkish.  
[Ukrainian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Ukrainian.html) | Ukrainian.  
[Vietnamese](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Vietnamese.html) | Vietnamese.  
[ChineseSimplified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.ChineseSimplified.html) | ChineseSimplified.  
[ChineseTraditional](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.ChineseTraditional.html) | ChineseTraditional.  
[Hindi](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Hindi.html) | Hindi.  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Unknown.html) | Unknown.  
[Hungarian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.Hungarian.html) | Hungarian.  
* * *
