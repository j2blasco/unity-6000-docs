* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MobileKeyboard.html

  * [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html)
  * Mobile Keyboard


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html)
Input
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html)
Unity XR Input
# Mobile Keyboard
In most cases, Unity will handle keyboard input automatically for GUI elements but it is also easy to show the keyboard on demand from a script.
## GUI Elements
The keyboard will appear automatically when a user taps on editable GUI elements. Currently, [GUI.TextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextField.html), [GUI.TextArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.TextArea.html) and [GUI.PasswordField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.PasswordField.html) will display the keyboard; see the [GUI class](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) documentation for further details.
## Manual Keyboard Handling
Use the **[TouchScreenKeyboard.Open()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.Open.html)** function to open the keyboard. Please see the [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) scripting reference for the parameters that this function takes.
## Keyboard Layout Options
The Keyboard supports the following options:-
**_Property:_** | **_Function:_**  
---|---  
**[TouchScreenKeyboardType.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.Default.html)** | Letters. Can be switched to keyboard with numbers and punctuation.  
**[TouchScreenKeyboardType.ASCIICapable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.ASCIICapable.html)** | Letters. Can be switched to keyboard with numbers and punctuation.  
**[TouchScreenKeyboardType.NumbersAndPunctuation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.NumbersAndPunctuation.html)** | Numbers and punctuation. Can be switched to keyboard with letters.  
**[TouchScreenKeyboardType.URL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.URL.html)** | Letters with slash and .com buttons. Can be switched to keyboard with numbers and punctuation.  
**[TouchScreenKeyboardType.NumberPad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.NumberPad.html)** | Only numbers from 0 to 9.  
**[TouchScreenKeyboardType.PhonePad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.PhonePad.html)** | Keyboard used to enter phone numbers.  
**[TouchScreenKeyboardType.NamePhonePad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.NamePhonePad.html)** | Letters. Can be switched to phone keyboard.  
**[TouchScreenKeyboardType.EmailAddress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.EmailAddress.html)** | Letters with @ sign. Can be switched to keyboard with numbers and punctuation.  
## Text Preview
By default, an edit box will be created and placed on top of the keyboard after it appears. This works as preview of the text that user is typing, so the text is always visible for the user. However, you can disable text preview by setting **TouchScreenKeyboard.hideInput** to true. Note that this works only for certain keyboard types and input modes. For example, it will not work for phone keypads and multi-line text input. In such cases, the edit box will always appear. **TouchScreenKeyboard.hideInput** is a global variable and will affect all keyboards.
## Visibility and Keyboard Size
There are three keyboard properties in [TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) that determine keyboard visibility status and size on the screen.
**_Property:_** | **_Function:_**  
---|---  
**visible** | Returns **true** if the keyboard is fully visible on the screen and can be used to enter characters.  
**area** | Returns the position and dimensions of the keyboard.  
**active** | Returns **true** if the keyboard is activated. This property is not static property. You must have a keyboard instance to use this property.  
Note that **TouchScreenKeyboard.area** will return a Rect with position and size set to 0 until the keyboard is fully visible on the screen. You should not query this value immediately after **TouchScreenKeyboard.Open()**. The sequence of keyboard events is as follows:
  * **TouchScreenKeyboard.Open()** is called. **TouchScreenKeyboard.active** returns true. **TouchScreenKeyboard.visible** returns false. **TouchScreenKeyboard.area** returns (0, 0, 0, 0).
  * Keyboard slides out into the screen. All properties remain the same.
  * Keyboard stops sliding. **TouchScreenKeyboard.active** returns true. **TouchScreenKeyboard.visible** returns true. **TouchScreenKeyboard.area** returns real position and size of the keyboard.


## Secure Text Input
It is possible to configure the keyboard to hide symbols when typing. This is useful when users are required to enter sensitive information (such as passwords). To manually open keyboard with secure text input enabled, use the following code:
```
TouchScreenKeyboard.Open("", TouchScreenKeyboardType.Default, false, false, true);

```
![Hiding text while typing](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/KeyboardSecure.png) Hiding text while typing
## Alert keyboard
To display the keyboard with a black semi-transparent background instead of the classic opaque, call **TouchScreenKeyboard.Open()** as follows:
```
TouchScreenKeyboard.Open("", TouchScreenKeyboardType.Default, false, false, true, true);

```
![Alert keyboard](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/KeyboardAlert.png) Alert keyboard
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html)
Input
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html)
Unity XR Input
