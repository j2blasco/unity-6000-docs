* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-restrictions.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Scripting backends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
  * Scripting restrictions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/il2cpp-managed-stack-traces.html)
Managed stack traces with IL2CPP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/code-reloading-editor.html)
Code and scene reload on entering Play mode
# Scripting restrictions
Unity provides a common scripting API and experience across all platforms it supports. However, some platforms have inherent restrictions. To help you understand these restrictions, the following table describes which restrictions apply to each platform and **scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend):
**Platform (scripting backend)** | **Ahead-of-time compile** | **Supports threads**  
---|---|---  
Android (IL2CPP) | Yes | Yes  
Android (Mono) | No | Yes  
iOS (IL2CPP) | Yes | Yes  
Standalone (IL2CPP) | Yes | Yes  
Standalone (Mono) | No | Yes  
Universal Windows Platform (IL2CPP) | Yes | Yes  
Web (IL2CPP) | Yes | No  
## Ahead-of-time compile (AOT)
Some platforms don’t allow runtime code generation. Any managed code which depends upon just-in-time (JIT) compilation on the target device will fail. Instead, you must compile all the managed code ahead-of-time (AOT). Often, this distinction doesn’t matter, but in a few specific cases, AOT platforms require additional consideration.
### Reflection
Unity supports reflection on AOT platforms. However, if this compiler can’t infer that the code is used via reflection the code might not exist at runtime. For more information, refer to [Managed Code Stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html).
### System.Reflection.Emit
An AOT platform cannot implement any of the methods in the `System.Reflection.Emit` namespace.
### Serialization
AOT platforms might encounter issues with serialization and deserialization because of the use of reflection. If a type or method is only used via reflection as part of serialization or deserialization, the AOT compiler cannot detect that it needs to generate the code needs for the type or method.
### Generic Types and Methods
For generic types and methods the compiler must determine which generic instances are used because different generic instances might require different code. For example the code for `List<int>` is different than it is for `List<double>`. However IL2CPP will share code for usages for reference types, so the same code will be used for `List<object>` and `List<string>`.
It is possible to reference generic types and methods that **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) did not find a compile time in the following cases:
  1. Creating a new generic instance at runtime: `Activator.CreateInstance(typeof(SomeGenericType<>).MakeGenericType(someType));`
  2. Invoking a static method on a generic instance: `typeof(SomeGenericType<>).MakeGenericType(someType).GetMethod("AMethod").Invoke(null, null);`
  3. Invoking a static generic method: `typeof(SomeType).GetMethod("GenericMethod").MakeGenericMethod(someType).Invoke(null, null);`
  4. Some calls to generic virtual functions that cannot be inferred at compile time.
  5. Calls with deeply nested generic value types, such as `Struct<Struct<Struct<...<Struct<int>>>>`.


To support those cases IL2CPP generates generic code that will work with any type parameter. However this code is slower because it can make no assumptions on the size of the type or if it is a reference or value type. If you need to ensure that faster generic methods are generated, do the following:
  * If the generic argument will always be a reference type, add the `where: class` constraint. Then IL2CPP will generate the fallback method using reference type sharing which causes no performance degradation.
  * If the generic argument will always be a value type, add the `where: struct` constraint. This enables some optimizations, but the code will still be slower because the value types can be different sizes.
  * Create a method named `UsedOnlyForAOTCodeGeneration` and add references to the generic types and methods you wish IL2CPP to generate. This method does not need (and probably shouldn’t) be called. The example below will ensure that a specialization for `GenericType<MyStruct>` will be generated.

```
public void UsedOnlyForAOTCodeGeneration()
{
    // Ensure that IL2CPP will create code for MyGenericStruct
    // using MyStruct as an argument.
    new GenericType<MyStruct>();

    // Ensure that IL2CPP will create code for SomeType.GenericMethod
    // using MyStruct as an argument.
    new SomeType().GenericMethod<MyStruct>();

    public void OnMessage<T>(T value) 
    {
        Debug.LogFormat("Message value: {0}", value);
    }

    // Include an exception so we can be sure to know if this
    // method is ever called.
    throw new InvalidOperationException(
        "This method is used for AOT code generation only. " +
        "Do not call it at runtime.");
}

```

Note that when the “Optimize for code size and build time” setting is enabled only the single fully sharable version of generic code is compiled. This reduces the number of methods generated, reducing compile time and build size, but comes at the expense of runtime performance.
### Calling managed methods from native code
Managed methods that need to be marshaled to a C function pointer so that they can be called from native code have a few restrictions on AOT platforms:
  * The managed method must be a static method
  * The managed method must have the `[MonoPInvokeCallback]` attribute
  * If the managed method is generic, the `[MonoPInvokeCallback(Type)]` overload might need to be used to specify the generic specializations that need to be supported. If so, the type must be a generic instance with the correct number of generic arguments. It’s possible to have multiple `[MonoPInvokeCallback]` attributes on a method as below:

```
// Generates reverse P/Invoke wrappers for NameOf<long> and NameOf<int>
// Note that the types are only used to indicate the generic arguments.
[MonoPInvokeCallback(typeof(Action<long>))]
[MonoPInvokeCallback(typeof(Action<int>))]
private static string NameOfT<T>(T item) 
{
    return typeof(T).Name;
}

```

## No threads
Some platforms do not support the use of threads, so any managed code that uses the `System.Threading` namespace fails at runtime. Also, some parts of the .NET class libraries implicitly depend upon threads. An often-used example is the `System.Timers.Timer` class, which depends on support for threads.
## Exception filters
IL2CPP supports exception filters, however the execution order filter statements and catch blocks is different because IL2CPP uses C++ exceptions to implement managed exceptions. This will not be noticeable unless a filter blocks writes to a field.
## MarshalAs and FieldOffset attributes
IL2CPP does not support reflection of the `MarshalAs` and `FieldOffset` attributes at runtime. It does support these attributes at compile time. You should use these for proper [platform invoke marshaling](https://docs.microsoft.com/en-us/dotnet/framework/interop/marshaling-data-with-platform-invoke).
## The dynamic keyword
IL2CPP does not support the C# `dynamic` keyword. This keyword requires JIT compilation, which is not possible with IL2CPP.
## Marshal.Prelink
IL2CPP doesn’t support the `Marshal.Prelink` or `Marshal.PrelinkAll` API methods.
## System.Diagnostics.Process API
IL2CPP doesn’t support the `System.Diagnostics.Process` API methods. For cases where this is required on desktop platforms, use the Mono scripting backend.
## Additonal resources
  * [Unity .NET features](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/il2cpp-managed-stack-traces.html)
Managed stack traces with IL2CPP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/code-reloading-editor.html)
Code and scene reload on entering Play mode
