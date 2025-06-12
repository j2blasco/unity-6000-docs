* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html

# KeyCode
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
Key codes returned by [Event.keyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-keyCode.html). These map directly to a physical key on the keyboard. If "Use Physical Keys" is enabled in [Input Manager settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html), these map directly to a physical key on the keyboard. If "Use Physical Keys" is disabled these map to language dependent mapping, different for every platform and cannot be guaranteed to work. "Use Physical Keys" is enabled by default from 2022.1
Key codes can be used to detect key down and key up events, using [Input.GetKeyDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html) and [Input.GetKeyUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html):
```
using UnityEngine;  
  
public class KeyCodeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key was pressed.");
        }  
  
        if (Input.GetKeyUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyUp.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key was released.");
        }
    }
}

```

Keyboard events can also be captured within `OnGUI`:
```
using UnityEngine;  
  
public class KeyCodeOnGUIExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (Event.current.Equals(Event.KeyboardEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.KeyboardEvent.html)(KeyCode.Space.ToString())))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) key is pressed.");
        }
    }
}

```

For joystick and gamepad button presses, consider using [Input.GetButtonDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html) and [Input.GetButtonUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonUp.html) instead of the KeyCode. These methods allow you to check input state using a descriptive action string, e.g. "fire" or "jump", instead of the hardware button number.  
  
The [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) pages provide details about accessing keyboard, mouse and joystick input.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.None.html) | Not assigned (never returned as the result of a keystroke).  
[Backspace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Backspace.html) | The backspace key.  
[Delete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Delete.html) | The forward delete key.  
[Tab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Tab.html) | The tab key.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Clear.html) | The Clear key.  
[Return](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Return.html) | Return key.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Pause.html) | Pause on PC machines.  
[Escape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Escape.html) | Escape key.  
[Space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html) | Space key.  
[Keypad0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad0.html) | Numeric keypad 0.  
[Keypad1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad1.html) | Numeric keypad 1.  
[Keypad2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad2.html) | Numeric keypad 2.  
[Keypad3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad3.html) | Numeric keypad 3.  
[Keypad4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad4.html) | Numeric keypad 4.  
[Keypad5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad5.html) | Numeric keypad 5.  
[Keypad6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad6.html) | Numeric keypad 6.  
[Keypad7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad7.html) | Numeric keypad 7.  
[Keypad8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad8.html) | Numeric keypad 8.  
[Keypad9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Keypad9.html) | Numeric keypad 9.  
[KeypadPeriod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadPeriod.html) | Numeric keypad '.'.  
[KeypadDivide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadDivide.html) | Numeric keypad '/'.  
[KeypadMultiply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadMultiply.html) | Numeric keypad '*'.  
[KeypadMinus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadMinus.html) | Numeric keypad '-'.  
[KeypadPlus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadPlus.html) | Numeric keypad '+'.  
[KeypadEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadEnter.html) | Numeric keypad Enter.  
[KeypadEquals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.KeypadEquals.html) | Numeric keypad '='.  
[UpArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.UpArrow.html) | Up arrow key.  
[DownArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DownArrow.html) | Down arrow key.  
[RightArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightArrow.html) | Right arrow key.  
[LeftArrow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftArrow.html) | Left arrow key.  
[Insert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Insert.html) | Insert key key.  
[Home](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Home.html) | Home key.  
[End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.End.html) | End key.  
[PageUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.PageUp.html) | Page up.  
[PageDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.PageDown.html) | Page down.  
[F1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F1.html) | F1 function key.  
[F2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F2.html) | F2 function key.  
[F3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F3.html) | F3 function key.  
[F4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F4.html) | F4 function key.  
[F5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F5.html) | F5 function key.  
[F6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F6.html) | F6 function key.  
[F7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F7.html) | F7 function key.  
[F8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F8.html) | F8 function key.  
[F9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F9.html) | F9 function key.  
[F10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F10.html) | F10 function key.  
[F11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F11.html) | F11 function key.  
[F12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F12.html) | F12 function key.  
[F13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F13.html) | F13 function key.  
[F14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F14.html) | F14 function key.  
[F15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F15.html) | F15 function key.  
[Alpha0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha0.html) | The '0' key on the top of the alphanumeric keyboard.  
[Alpha1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha1.html) | The '1' key on the top of the alphanumeric keyboard.  
[Alpha2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha2.html) | The '2' key on the top of the alphanumeric keyboard.  
[Alpha3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha3.html) | The '3' key on the top of the alphanumeric keyboard.  
[Alpha4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha4.html) | The '4' key on the top of the alphanumeric keyboard.  
[Alpha5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha5.html) | The '5' key on the top of the alphanumeric keyboard.  
[Alpha6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha6.html) | The '6' key on the top of the alphanumeric keyboard.  
[Alpha7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha7.html) | The '7' key on the top of the alphanumeric keyboard.  
[Alpha8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha8.html) | The '8' key on the top of the alphanumeric keyboard.  
[Alpha9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Alpha9.html) | The '9' key on the top of the alphanumeric keyboard.  
[Exclaim](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Exclaim.html) | Exclamation mark key '!'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha1 instead.  
[DoubleQuote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.DoubleQuote.html) | Double quote key '"'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Quote instead.  
[Hash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Hash.html) | Hash key '#'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha3 instead.  
[Dollar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Dollar.html) | Dollar sign key '$'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha4 instead.  
[Percent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Percent.html) | Percent '%' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha5 instead.  
[Ampersand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Ampersand.html) | Ampersand key '&'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha7 instead.  
[Quote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Quote.html) | Quote key '.  
[LeftParen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftParen.html) | Left Parenthesis key '('. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha9 instead.  
[RightParen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightParen.html) | Right Parenthesis key ')'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha0 instead.  
[Asterisk](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Asterisk.html) | Asterisk key '*'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha8 instead.  
[Plus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Plus.html) | Plus key '+'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Equals instead.  
[Comma](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Comma.html) | Comma ',' key.  
[Minus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Minus.html) | Minus '-' key.  
[Period](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Period.html) | Period '.' key.  
[Slash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Slash.html) | Slash '/' key.  
[Colon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Colon.html) | Colon ':' key.Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Semicolon instead.  
[Semicolon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Semicolon.html) | Semicolon ';' key.  
[Less](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Less.html) | Less than '<' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Comma instead.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Equals.html) | Equals '=' key.  
[Greater](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Greater.html) | Greater than '>' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Period instead.  
[Question](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Question.html) | Question mark '?' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Slash instead.  
[At](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.At.html) | At key '@'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha2 instead.  
[LeftBracket](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftBracket.html) | Left square bracket key '['.  
[Backslash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Backslash.html) | Backslash key '\'.  
[RightBracket](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightBracket.html) | Right square bracket key ']'.  
[Caret](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Caret.html) | Caret key '^'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Alpha6 instead.  
[Underscore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Underscore.html) | Underscore '_' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Minus instead.  
[BackQuote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.BackQuote.html) | Back quote key '`'.  
[A](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.A.html) | 'a' key.  
[B](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.B.html) | 'b' key.  
[C](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.C.html) | 'c' key.  
[D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.D.html) | 'd' key.  
[E](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.E.html) | 'e' key.  
[F](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F.html) | 'f' key.  
[G](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.G.html) | 'g' key.  
[H](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.H.html) | 'h' key.  
[I](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.I.html) | 'i' key.  
[J](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.J.html) | 'j' key.  
[K](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.K.html) | 'k' key.  
[L](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.L.html) | 'l' key.  
[M](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.M.html) | 'm' key.  
[N](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.N.html) | 'n' key.  
[O](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.O.html) | 'o' key.  
[P](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.P.html) | 'p' key.  
[Q](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Q.html) | 'q' key.  
[R](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.R.html) | 'r' key.  
[S](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.S.html) | 's' key.  
[T](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.T.html) | 't' key.  
[U](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.U.html) | 'u' key.  
[V](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.V.html) | 'v' key.  
[W](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.W.html) | 'w' key.  
[X](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.X.html) | 'x' key.  
[Y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Y.html) | 'y' key.  
[Z](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Z.html) | 'z' key.  
[LeftCurlyBracket](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftCurlyBracket.html) | Left curly bracket key '{'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.LeftBracket instead.  
[Pipe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Pipe.html) | Pipe '|' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.Backslash instead.  
[RightCurlyBracket](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightCurlyBracket.html) | Right curly bracket key '}'. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.RightBracket instead.  
[Tilde](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Tilde.html) | Tilde '~' key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.BackQuote instead.  
[Numlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Numlock.html) | Numlock key.  
[CapsLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.CapsLock.html) | Capslock key.  
[ScrollLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.ScrollLock.html) | Scroll lock key.  
[RightShift](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightShift.html) | Right shift key.  
[LeftShift](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftShift.html) | Left shift key.  
[RightControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightControl.html) | Right Control key.  
[LeftControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftControl.html) | Left Control key.  
[RightAlt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightAlt.html) | Right Alt key.  
[LeftAlt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftAlt.html) | Left Alt key.  
[LeftMeta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftMeta.html) | Maps to left Windows key or left Command key if physical keys are enabled in Input Manager settings, otherwise maps to left Command key only.  
[LeftCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftCommand.html) | Left Command key.  
[LeftApple](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftApple.html) | Left Command key.  
[LeftWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftWindows.html) | Left Windows key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.LeftMeta instead.  
[RightMeta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightMeta.html) | Maps to right Windows key or right Command key if physical keys are enabled in Input Manager settings, otherwise maps to right Command key only.  
[RightCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightCommand.html) | Right Command key.  
[RightApple](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightApple.html) | Right Command key.  
[RightWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightWindows.html) | Right Windows key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.RightMeta instead.  
[AltGr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.AltGr.html) | Alt Gr key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, use KeyCode.RightAlt instead.  
[Help](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Help.html) | Help key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, doesn't map to any physical key.  
[Print](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Print.html) | Print key.  
[SysReq](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.SysReq.html) | Sys Req key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, doesn't map to any physical key.  
[Break](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Break.html) | Break key. Deprecated if "Use Physical Keys" is enabled in Input Manager settings, doesn't map to any physical key.  
[Menu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Menu.html) | Menu key.  
[WheelUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.WheelUp.html) | Mouse wheel up.  
[WheelDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.WheelDown.html) | Mouse wheel down.  
[F16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F16.html) | F16 function key.  
[F17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F17.html) | F17 function key.  
[F18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F18.html) | F18 function key.  
[F19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F19.html) | F19 function key.  
[F20](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F20.html) | F20 function key.  
[F21](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F21.html) | F21 function key.  
[F22](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F22.html) | F22 function key.  
[F23](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F23.html) | F23 function key.  
[F24](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.F24.html) | F24 function key.  
[Mouse0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse0.html) | The Left (or primary) mouse button.  
[Mouse1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse1.html) | Right mouse button (or secondary mouse button).  
[Mouse2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse2.html) | Middle mouse button (or third button).  
[Mouse3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse3.html) | Additional (fourth) mouse button.  
[Mouse4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse4.html) | Additional (fifth) mouse button.  
[Mouse5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse5.html) | Additional (or sixth) mouse button.  
[Mouse6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Mouse6.html) | Additional (or seventh) mouse button.  
[JoystickButton0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton0.html) | Button 0 on any joystick.  
[JoystickButton1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton1.html) | Button 1 on any joystick.  
[JoystickButton2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton2.html) | Button 2 on any joystick.  
[JoystickButton3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton3.html) | Button 3 on any joystick.  
[JoystickButton4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton4.html) | Button 4 on any joystick.  
[JoystickButton5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton5.html) | Button 5 on any joystick.  
[JoystickButton6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton6.html) | Button 6 on any joystick.  
[JoystickButton7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton7.html) | Button 7 on any joystick.  
[JoystickButton8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton8.html) | Button 8 on any joystick.  
[JoystickButton9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton9.html) | Button 9 on any joystick.  
[JoystickButton10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton10.html) | Button 10 on any joystick.  
[JoystickButton11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton11.html) | Button 11 on any joystick.  
[JoystickButton12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton12.html) | Button 12 on any joystick.  
[JoystickButton13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton13.html) | Button 13 on any joystick.  
[JoystickButton14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton14.html) | Button 14 on any joystick.  
[JoystickButton15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton15.html) | Button 15 on any joystick.  
[JoystickButton16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton16.html) | Button 16 on any joystick.  
[JoystickButton17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton17.html) | Button 17 on any joystick.  
[JoystickButton18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton18.html) | Button 18 on any joystick.  
[JoystickButton19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.JoystickButton19.html) | Button 19 on any joystick.  
[Joystick1Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button0.html) | Button 0 on first joystick.  
[Joystick1Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button1.html) | Button 1 on first joystick.  
[Joystick1Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button2.html) | Button 2 on first joystick.  
[Joystick1Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button3.html) | Button 3 on first joystick.  
[Joystick1Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button4.html) | Button 4 on first joystick.  
[Joystick1Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button5.html) | Button 5 on first joystick.  
[Joystick1Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button6.html) | Button 6 on first joystick.  
[Joystick1Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button7.html) | Button 7 on first joystick.  
[Joystick1Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button8.html) | Button 8 on first joystick.  
[Joystick1Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button9.html) | Button 9 on first joystick.  
[Joystick1Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button10.html) | Button 10 on first joystick.  
[Joystick1Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button11.html) | Button 11 on first joystick.  
[Joystick1Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button12.html) | Button 12 on first joystick.  
[Joystick1Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button13.html) | Button 13 on first joystick.  
[Joystick1Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button14.html) | Button 14 on first joystick.  
[Joystick1Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button15.html) | Button 15 on first joystick.  
[Joystick1Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button16.html) | Button 16 on first joystick.  
[Joystick1Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button17.html) | Button 17 on first joystick.  
[Joystick1Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button18.html) | Button 18 on first joystick.  
[Joystick1Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick1Button19.html) | Button 19 on first joystick.  
[Joystick2Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button0.html) | Button 0 on second joystick.  
[Joystick2Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button1.html) | Button 1 on second joystick.  
[Joystick2Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button2.html) | Button 2 on second joystick.  
[Joystick2Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button3.html) | Button 3 on second joystick.  
[Joystick2Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button4.html) | Button 4 on second joystick.  
[Joystick2Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button5.html) | Button 5 on second joystick.  
[Joystick2Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button6.html) | Button 6 on second joystick.  
[Joystick2Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button7.html) | Button 7 on second joystick.  
[Joystick2Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button8.html) | Button 8 on second joystick.  
[Joystick2Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button9.html) | Button 9 on second joystick.  
[Joystick2Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button10.html) | Button 10 on second joystick.  
[Joystick2Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button11.html) | Button 11 on second joystick.  
[Joystick2Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button12.html) | Button 12 on second joystick.  
[Joystick2Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button13.html) | Button 13 on second joystick.  
[Joystick2Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button14.html) | Button 14 on second joystick.  
[Joystick2Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button15.html) | Button 15 on second joystick.  
[Joystick2Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button16.html) | Button 16 on second joystick.  
[Joystick2Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button17.html) | Button 17 on second joystick.  
[Joystick2Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button18.html) | Button 18 on second joystick.  
[Joystick2Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick2Button19.html) | Button 19 on second joystick.  
[Joystick3Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button0.html) | Button 0 on third joystick.  
[Joystick3Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button1.html) | Button 1 on third joystick.  
[Joystick3Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button2.html) | Button 2 on third joystick.  
[Joystick3Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button3.html) | Button 3 on third joystick.  
[Joystick3Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button4.html) | Button 4 on third joystick.  
[Joystick3Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button5.html) | Button 5 on third joystick.  
[Joystick3Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button6.html) | Button 6 on third joystick.  
[Joystick3Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button7.html) | Button 7 on third joystick.  
[Joystick3Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button8.html) | Button 8 on third joystick.  
[Joystick3Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button9.html) | Button 9 on third joystick.  
[Joystick3Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button10.html) | Button 10 on third joystick.  
[Joystick3Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button11.html) | Button 11 on third joystick.  
[Joystick3Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button12.html) | Button 12 on third joystick.  
[Joystick3Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button13.html) | Button 13 on third joystick.  
[Joystick3Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button14.html) | Button 14 on third joystick.  
[Joystick3Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button15.html) | Button 15 on third joystick.  
[Joystick3Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button16.html) | Button 16 on third joystick.  
[Joystick3Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button17.html) | Button 17 on third joystick.  
[Joystick3Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button18.html) | Button 18 on third joystick.  
[Joystick3Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick3Button19.html) | Button 19 on third joystick.  
[Joystick4Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button0.html) | Button 0 on forth joystick.  
[Joystick4Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button1.html) | Button 1 on forth joystick.  
[Joystick4Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button2.html) | Button 2 on forth joystick.  
[Joystick4Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button3.html) | Button 3 on forth joystick.  
[Joystick4Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button4.html) | Button 4 on forth joystick.  
[Joystick4Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button5.html) | Button 5 on forth joystick.  
[Joystick4Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button6.html) | Button 6 on forth joystick.  
[Joystick4Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button7.html) | Button 7 on forth joystick.  
[Joystick4Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button8.html) | Button 8 on forth joystick.  
[Joystick4Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button9.html) | Button 9 on forth joystick.  
[Joystick4Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button10.html) | Button 10 on forth joystick.  
[Joystick4Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button11.html) | Button 11 on forth joystick.  
[Joystick4Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button12.html) | Button 12 on forth joystick.  
[Joystick4Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button13.html) | Button 13 on forth joystick.  
[Joystick4Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button14.html) | Button 14 on forth joystick.  
[Joystick4Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button15.html) | Button 15 on forth joystick.  
[Joystick4Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button16.html) | Button 16 on forth joystick.  
[Joystick4Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button17.html) | Button 17 on forth joystick.  
[Joystick4Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button18.html) | Button 18 on forth joystick.  
[Joystick4Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick4Button19.html) | Button 19 on forth joystick.  
[Joystick5Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button0.html) | Button 0 on fifth joystick.  
[Joystick5Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button1.html) | Button 1 on fifth joystick.  
[Joystick5Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button2.html) | Button 2 on fifth joystick.  
[Joystick5Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button3.html) | Button 3 on fifth joystick.  
[Joystick5Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button4.html) | Button 4 on fifth joystick.  
[Joystick5Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button5.html) | Button 5 on fifth joystick.  
[Joystick5Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button6.html) | Button 6 on fifth joystick.  
[Joystick5Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button7.html) | Button 7 on fifth joystick.  
[Joystick5Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button8.html) | Button 8 on fifth joystick.  
[Joystick5Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button9.html) | Button 9 on fifth joystick.  
[Joystick5Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button10.html) | Button 10 on fifth joystick.  
[Joystick5Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button11.html) | Button 11 on fifth joystick.  
[Joystick5Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button12.html) | Button 12 on fifth joystick.  
[Joystick5Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button13.html) | Button 13 on fifth joystick.  
[Joystick5Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button14.html) | Button 14 on fifth joystick.  
[Joystick5Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button15.html) | Button 15 on fifth joystick.  
[Joystick5Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button16.html) | Button 16 on fifth joystick.  
[Joystick5Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button17.html) | Button 17 on fifth joystick.  
[Joystick5Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button18.html) | Button 18 on fifth joystick.  
[Joystick5Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick5Button19.html) | Button 19 on fifth joystick.  
[Joystick6Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button0.html) | Button 0 on sixth joystick.  
[Joystick6Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button1.html) | Button 1 on sixth joystick.  
[Joystick6Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button2.html) | Button 2 on sixth joystick.  
[Joystick6Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button3.html) | Button 3 on sixth joystick.  
[Joystick6Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button4.html) | Button 4 on sixth joystick.  
[Joystick6Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button5.html) | Button 5 on sixth joystick.  
[Joystick6Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button6.html) | Button 6 on sixth joystick.  
[Joystick6Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button7.html) | Button 7 on sixth joystick.  
[Joystick6Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button8.html) | Button 8 on sixth joystick.  
[Joystick6Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button9.html) | Button 9 on sixth joystick.  
[Joystick6Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button10.html) | Button 10 on sixth joystick.  
[Joystick6Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button11.html) | Button 11 on sixth joystick.  
[Joystick6Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button12.html) | Button 12 on sixth joystick.  
[Joystick6Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button13.html) | Button 13 on sixth joystick.  
[Joystick6Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button14.html) | Button 14 on sixth joystick.  
[Joystick6Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button15.html) | Button 15 on sixth joystick.  
[Joystick6Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button16.html) | Button 16 on sixth joystick.  
[Joystick6Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button17.html) | Button 17 on sixth joystick.  
[Joystick6Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button18.html) | Button 18 on sixth joystick.  
[Joystick6Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick6Button19.html) | Button 19 on sixth joystick.  
[Joystick7Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button0.html) | Button 0 on seventh joystick.  
[Joystick7Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button1.html) | Button 1 on seventh joystick.  
[Joystick7Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button2.html) | Button 2 on seventh joystick.  
[Joystick7Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button3.html) | Button 3 on seventh joystick.  
[Joystick7Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button4.html) | Button 4 on seventh joystick.  
[Joystick7Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button5.html) | Button 5 on seventh joystick.  
[Joystick7Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button6.html) | Button 6 on seventh joystick.  
[Joystick7Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button7.html) | Button 7 on seventh joystick.  
[Joystick7Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button8.html) | Button 8 on seventh joystick.  
[Joystick7Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button9.html) | Button 9 on seventh joystick.  
[Joystick7Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button10.html) | Button 10 on seventh joystick.  
[Joystick7Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button11.html) | Button 11 on seventh joystick.  
[Joystick7Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button12.html) | Button 12 on seventh joystick.  
[Joystick7Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button13.html) | Button 13 on seventh joystick.  
[Joystick7Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button14.html) | Button 14 on seventh joystick.  
[Joystick7Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button15.html) | Button 15 on seventh joystick.  
[Joystick7Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button16.html) | Button 16 on seventh joystick.  
[Joystick7Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button17.html) | Button 17 on seventh joystick.  
[Joystick7Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button18.html) | Button 18 on seventh joystick.  
[Joystick7Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick7Button19.html) | Button 19 on seventh joystick.  
[Joystick8Button0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button0.html) | Button 0 on eighth joystick.  
[Joystick8Button1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button1.html) | Button 1 on eighth joystick.  
[Joystick8Button2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button2.html) | Button 2 on eighth joystick.  
[Joystick8Button3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button3.html) | Button 3 on eighth joystick.  
[Joystick8Button4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button4.html) | Button 4 on eighth joystick.  
[Joystick8Button5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button5.html) | Button 5 on eighth joystick.  
[Joystick8Button6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button6.html) | Button 6 on eighth joystick.  
[Joystick8Button7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button7.html) | Button 7 on eighth joystick.  
[Joystick8Button8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button8.html) | Button 8 on eighth joystick.  
[Joystick8Button9](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button9.html) | Button 9 on eighth joystick.  
[Joystick8Button10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button10.html) | Button 10 on eighth joystick.  
[Joystick8Button11](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button11.html) | Button 11 on eighth joystick.  
[Joystick8Button12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button12.html) | Button 12 on eighth joystick.  
[Joystick8Button13](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button13.html) | Button 13 on eighth joystick.  
[Joystick8Button14](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button14.html) | Button 14 on eighth joystick.  
[Joystick8Button15](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button15.html) | Button 15 on eighth joystick.  
[Joystick8Button16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button16.html) | Button 16 on eighth joystick.  
[Joystick8Button17](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button17.html) | Button 17 on eighth joystick.  
[Joystick8Button18](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button18.html) | Button 18 on eighth joystick.  
[Joystick8Button19](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Joystick8Button19.html) | Button 19 on eighth joystick.  
* * *
