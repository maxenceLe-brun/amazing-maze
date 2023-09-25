# amazing-maze

This is a recap of my journey building this program !
Unfortunately, some of my work vanished due to a BSoD and my spyder didn't process the autosave of the end of my kruskal's algo and the full code of the aStar too :/
So, big my bad, and i accept the fact that i didn't finished the work correctly

## Context

So, first things first, i was planning on making 3 class : the class Case, the class BackTrack, and the class Special.
For the Case, i already thought about my entire class correctly : 7 variables : (x,y) for the coordinates; (u,d,l,r) for each wall of my labyrinth and (already) to state if the case was used or not.
Then, i started my backtracking code, but how do i know when it did the things i would do or not? This is the first problem i was stuck on, and directly worked on the printing
The function "show()" is simple but complicated at the same time : it simply print each case with all of the characters between alt+185 and alt+188, and alt+200 and alt+206 (╣ ║ ╗ ╗ ╚ ╔ ╩ ╦ ╠ ═ ╬)
Then, i came back to my backtrack creation, and worked on the third time, with just some errors in my calculs
For the solving code backtrack, it wasn't really a big deal, i used barely the same system as the labyrinth creation, with some modifications such as the choice of directions and the stored path.

Let's go into the kruskal algo : It was a big big deal cuz it made me remake it 4 times in a row, the 3rd time was pretty good but the 4th time, a friend told me that a good example was in the documentation of the project, so i followed the same example with some tips given by Sacia, like the numbers attribued to each cases to make a good render

i can't really talk about aStar because i don't have the script to follow the same schematic, but i was struggling into the node system, the openned list memory and closed list memory 
