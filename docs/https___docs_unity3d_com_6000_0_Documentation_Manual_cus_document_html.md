* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/cus-document.html

  * [Packages and package management](https://docs.unity3d.com/6000.0/Documentation/Manual/PackagesList.html)
  * [Create custom packages](https://docs.unity3d.com/6000.0/Documentation/Manual/CustomPackages.html)
  * Document your package


[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-legal.html)
Custom package legal requirements
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-share.html)
Share your package
# Document your package
Most packages need some form of explanation to help users have the best experience and optimize its use. This page provides some tips for how to [structure the information](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-document.html#doc_structure) and [format the documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-document.html#doc_format). 
## Structure of the information
After the title of the package, give a basic overview of the package and its contents. Following the overview and package contents, include instructions for installing, system requirements, and limitations. You can also offer links for getting help and providing feedback, including public forums or knowledge bases, and support contacts.
After this preliminary information, you can offer more in-depth workflows, description of the user interface or directory listings for samples, and then more advanced topics. It’s best to offer reference pages near the end.
**Section** | **Description**  
---|---  
**Overview** | A brief, high-level explanation of the package.  
**Package contents** | Include the location of important files you want the user to know about. For example, if this is a sample package containing textures, models, and materials separated by sample group, you might want to specify the folder location of each group.  
**Installation instructions** | You can point to the official [Package Manager installation instructions](https://docs.unity3d.com/Manual/upm-ui-install.html), but if you have any special installation requirements, such as installing samples, add them here.  
**Requirements** | This is a good place to add hardware or software requirements, including which versions of the Unity Editor this package is compatible with.  
**Limitations** | If your package has any known limitations, you can list them here. If not, or if the limitations are trivial, exclude this section.  
**Workflows** | Include a list of steps that the user can follow that demonstrates how to use the feature. You can include screenshots to help describe how to use the feature.  
**Advanced topics** | Detailed information about what you’re providing to users. This is ideal if you don’t want to overwhelm the user with too much information up front.  
**Reference** | If you have a user interface with a lot of properties, you can describe their details in a reference section. Using tables is a good way to offer specific property descriptions.  
**Samples** | For packages that include sample files, you can include detailed information on how the user can use these sample files in their projects and **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
**Tutorials** | If you want to offer walk-throughs for complicated procedures, you can also add them here. Use step-by-step instructions and include images if they can help the user understand.  
## Documentation format
Markdown is a lightweight format commonly used in packages. Many repository hosting services (such as GitHub and Bitbucket) support Markdown for `README` files and documentation sites. You can include a Markdown file in the `Documentation~` folder under your package root. Then, when a user clicks the **Documentation** link in the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html) of Unity’s Package Manager window, the user’s default Markdown viewer opens the file.
You can also use your own website to host your documentation. To set the location for the **Documentation** link to point to your own website, set it with the [documentationUrl](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html#documentationUrl) property in your `package.json` file.
If you decide to use Markdown to document your package, you can find information about writing Markdown files from many sites, including:
  * The [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
  * [Bitbucket’s tutorial](https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html)
  * [GitHub’s Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-legal.html)
Custom package legal requirements
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cus-share.html)
Share your package
