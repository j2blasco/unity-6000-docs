* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-assemblies.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Environment and tools](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
  * [Unity .NET features](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
  * Referencing additional class library assemblies


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html)
Third-party .NET libraries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/csharp-compiler.html)
C# compiler
# Referencing additional class library assemblies
If your Unity project uses a part of the .NET class library API that Unity doesn’t compile by default, you can provide the C# compiler with a list of additional assemblies to reference during compilation. The behavior depends on which .NET profile the project uses. For more information, see [.NET Profile support](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html).
## .NET Standard profile
If your project uses the .NET Standard profile, all parts of the .NET class library API are referenced by default. You can’t reference additional assemblies. If part of the API seems to be missing, it might not be included with .NET Standard. Try using the .NET Framework profile instead. To avoid compilation problems when you change profiles, see [Switching between profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-assemblies.html#SwitchingBetweenProfiles).
## .NET Framework profile
By default, Unity references the following assemblies when you use the .NET Framework profile:
  * mscorlib.dll
  * System.dll
  * System.Core.dll
  * System.Runtime.Serialization.dll
  * System.Xml.dll
  * System.Xml.Linq.dll


To reference any other class library assemblies, use a csc.rsp file: a response file that contains a list of command line arguments that you can pass to the C# compiler. To use a csc.rsp file, follow the below instructions:
  1. Create a file named csc.rsp in the `Assets` folder of your Unity project.
  2. Move any assembly files you want to reference into the `Assets` folder of your project, if they aren’t already in this folder.
  3. Populate the csc.rsp file with command line arguments for the assemblies you want to reference.


For example, if your project uses the `HttpClient` class, which is defined in the `System.Net.Http.dll` assembly, the C# compiler might produce this initial error message if the assembly isn’t present:
```

The type `HttpClient` is defined in an assembly that is not referenced. You must add a reference to assembly 'System.Net.Http, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a'.


```

To resolve this error, add a csc.rsp file that contains the following command line argument to the project:
```

-r:System.Net.Http.dll


```

Add a new line with the appropriate command line argument for each assembly you want to reference.
## Switching between profiles
When you use a csc.rsp file to reference class library assemblies and you change the .NET profile, you might experience compilation problems.
If you change the .NET profile from .NET Framework to .NET Standard and your csc.rsp file references an assembly that doesn’t exist in the .NET Standard profile, then compilation fails. To solve the issue, edit the csc.rsp file to remove any references to assemblies that are exclusive to the .NET Framework profile before you change the .NET profile to .NET Standard.
## Additional resources
  * [.NET Profile Support](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html).
  * [.NET System libraries](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html).
  * [Third-party .NET libraries](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html)
Third-party .NET libraries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/csharp-compiler.html)
C# compiler
