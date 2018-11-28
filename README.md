# clarisse-drop
Clarisse iFX - "preset" saver - manager with MongoDB as backend, Python 2.7, MongoDB

This tool is under heavy development. It was born from my need to reuse stuff I exprimented and made in Clarisse for a faster workflow.
I do spend my spare time on this and would appreciate if anyone is interested joining the effort to refine it to its full potential.


Basic concept:

Select any object, context or shading network, clik Store and add it a name or comment.
You can bring back your saved selection easily by clicking Paster and choosing one or muiltiple entries and your 
saved selection is brought back to your project.

What this tool is not?
This tool is not an asset managment system/manager.


Scenario:

You have setup complex scatter setup you want to reuse, simply select what you want to save and store it. 
You can recall it anytime when you need it back in any project.

You have a complex shading network you want to template but not instance it from another project, simply save it and
recall and replace your textures or nodes. 

You want to save youre building blocks for your next project?
Like setup Images and contextexts with lights, camera setups, light linked groups and ... you can.



All your data is saved as Clarisse serialized content, that means pure text format Clarisse understands.
This tool levarages on copy / paste those snippets and storing them as encrypted objects in MongoDB.

This tool features encryption and decryption of saved content, so no one without a key cannot read your data.
Beware, youre key is unique and without it you cannot decrypt your saves. 

Support for flat-file format or JSON could be implemented instead of using MongoDB, but i wanted a robust and schema free DB.
Support for custom fields / attributes could added be too. Would love some requests and ideas.

There is no creation of users or separate mongo collections yet. As soon i wrote those i will let this tool live on github.
It only works on Windows for now, but i will port it to Unix and MacOS X soon.


Those who would like to contribute open and issue and let me know so we can crunch it together, you get a Discord invite for free :)




