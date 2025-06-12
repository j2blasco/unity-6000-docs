* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-pinvoke.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * [IL2CPP scripting backend for UWP](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-scripting.html)
  * [Use UWP plug-ins with IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-plugins.html)
  * Use P/Invoke


[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-native-plugins-author.html)
Author native UWP plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-debugging.html)
Debug UWP applications with IL2CPP
# Use P/Invoke
P/Invoke is a technology that allows you to access structs, callbacks, and functions in native code from your managed code. The default calling convention for P/Invoke functions on x86 is `__stdcall`. For more information, refer to Microsoft documentation on [P/Invoke](https://learn.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke).
## P/invoke marshaling rules
P/Invoke marshaling rules are the same as those for [.NET marshaling](https://learn.microsoft.com/en-us/dotnet/standard/native-interop/type-marshalling). However, Unity doesn’t support the following types:
  * AnsiBStr
  * Currency
  * SAFEARRAY
  * IDispatch
  * TBStr
  * VBByRefStr


## P/invoke limitations
On Universal Windows Platform (UWP), you can’t specify the dynamic-link library (DLL) name to P/Invoke into specific system libraries. If you try to P/Invoke into any DLL that exists outside of the project, it will result in a DllNotFoundException at runtime. Therefore, it’s possible to use the `__Internal` keyword in place of the DLL name, which will use the C++ linker to resolve the functions when you build your project, rather than when you load them at runtime:
```
    [DllImport("__Internal")]
    private static extern int CountLettersInString([MarshalAs(UnmanagedType.LPWStr)]string str);

```

If you make an error when you declare a function in your managed code, it will produce a linker error, rather than an error at runtime. This means that no dynamic loading needs to take place at runtime and the function is called directly, which decreases the overhead of a P/Invoke call.
## Additional resources
  * [Microsoft documentation on P/Invoke](https://learn.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke)
  * [Author native UWP plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-native-plugins-author.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-native-plugins-author.html)
Author native UWP plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-debugging.html)
Debug UWP applications with IL2CPP
