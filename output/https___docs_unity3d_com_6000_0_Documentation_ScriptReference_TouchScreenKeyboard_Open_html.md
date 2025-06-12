* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html

#  [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html).Open
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
public static [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) Open(string text, [TouchScreenKeyboardType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.html) keyboardType = TouchScreenKeyboardType.Default, bool autocorrection = true, bool multiline = false, bool secure = false, bool alert = false, string textPlaceholder = "", int characterLimit = 0); 
### Parameters
Parameter | Description  
---|---  
text | Text to edit.  
keyboardType | Type of keyboard (eg, any text, numbers only, etc).  
autocorrection | Is autocorrection applied?  
multiline | Can more than one line of text be entered?  
secure | Is the text masked (for passwords, etc)?  
alert | Is the keyboard opened in alert mode?  
textPlaceholder | Text to be used if no other text is present.  
characterLimit | How many characters the keyboard input field is limited to. 0 = infinite. (Android and iOS only)  
### Description
Opens the native keyboard provided by OS on the screen.
The `autocorrection` determines whether the input tracks unknown words and suggests a more suitable replacement candidate to the user, replacing the typed text automatically unless the user explicitly overrides the action. The `multiline` determines if user can input more than one line of text. The `secure` identifies whether the keyboard is used for password. Text in the input field will be hidden from the user except the recently typed character. The keyboard can be opened in the `alert` mode too. The `placeholder` string will be displayed when there is no other text in the input field of the keyboard.  
  
Additional resources: [Alert keyboard](https://docs.unity3d.com/6000.0/Documentation/Manual/MobileKeyboard.html#alert)  
  

```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public string stringToEdit = "Hello World";
    private TouchScreenKeyboard[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) keyboard;  
  
    // Opens native keyboard
    void OnGUI()
    {
        stringToEdit = GUI.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 200, 30), stringToEdit, 30);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 50, 200, 100), "Default"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.Default.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 150, 200, 100), "ASCIICapable"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.ASCIICapable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.ASCIICapable.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 250, 200, 100), "Numbers and Punctuation"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.NumbersAndPunctuation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.NumbersAndPunctuation.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 350, 200, 100), "URL"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.URL[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.URL.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 450, 200, 100), "NumberPad"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.NumberPad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.NumberPad.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 550, 200, 100), "PhonePad"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.PhonePad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.PhonePad.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 650, 200, 100), "NamePhonePad"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.NamePhonePad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.NamePhonePad.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 750, 200, 100), "EmailAddress"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.EmailAddress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.EmailAddress.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 850, 200, 100), "Social"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.Social[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.Social.html));
        }
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 950, 200, 100), "Search"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.Search[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.Search.html));
        }
        // Only supported on iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 1050, 200, 100), "One Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) Code"))
        {
            keyboard = TouchScreenKeyboard.Open[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)("", TouchScreenKeyboardType.OneTimeCode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.OneTimeCode.html));
        }
    }
}

```

* * *
