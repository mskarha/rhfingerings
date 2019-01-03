# Integer Programming for Optimal Right Hand Guitar Fingerings
By Matt Skarha, Isabel Taylor, and Mohit Dubey
----------------------------------------------------------------------------------------------
The Western canon of European classical music includes a substantial amount of scale-based, fingerstyle guitar music. When presented with a piece of sheet music, a classical guitarist must make a number of decisions regarding its performance. These decisions include notating the tablature, the left hand fingerings, and the right hand fingerings. This process, especially for right hand guitar fingerings, is often a trivial, yet cumbersome task. 

For example, consider the [*III. Allegro Solemne* movement](https://youtu.be/dmc6KV0_UVM?t=273) from the 1921 piece "La Catedral" by Paraguayan composer Agustín Barrios. Due to its fast tempo, the performer must pay careful attention to the fingerings to adhere to proper technique while maintaining such a tempo. The problem then becomes how can we use math and computer science to determine optimal fingerings for this type of music?

Bernd Tahon began to answer this question with this 2017 Master's thesis [*Fingers to frets - A Mathematical Approach*](https://vibeserver.net/scripties/2017/Fingers%20to%20Frets%20-%20Master%20Thesis%20Bernd%20Tahon.pdf) where he examined how to utilize math and computer science to optimize left hand finger assignments. In this project, we tackled the separate, yet related problem of right hand finger assignments. 

In fingerstyle music, the guitar is played using the thumb, index, middle, and ring fingers (not the pinky). At present, there is a notion within the classical guitar community of "proper right hand technique" which can be thought of as a set of rules that describe the physically optimal way of using the right hand to play scale-based, fingerstyle guitar music. These rules can be summarized as follows:

- Do not repeat fingers on consecutive notes
- The thumb plays the bassline
- Fingers stay in natural resting position
- Avoid backwards crossings
- Avoid ring-middle-ring alternation

We decided to formulate this problem as an integer program where each of these rules are a constraint imposed by the model. The integer program, then, consists of a minimization of a sum of penalty terms that are incurred by violating the "soft" constraints. The complete integer program can be found below: 

<center>
<img src="https://tex.s2cms.ru/svg/%5Ctext%7Bminimize%7D" alt="\text{minimize}" />
</center>

<center>
<img src="https://tex.s2cms.ru/svg/%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20p%5E%7BBC%7D_i%20%2B%20p%5ET_i%20%2B%20%5Cfrac%7B1%7D%7B2%7D%20p%5EF_i" alt="\sum_{i=1}^{n} p^{BC}_i + p^T_i + \frac{1}{2} p^F_i" />
</center>
<center>
<img src="https://tex.s2cms.ru/svg/%5Ctext%7Bsubject%20to%3A%7D" alt="\text{subject to:}" />
</center>
<center>
<img src="https://tex.s2cms.ru/svg/b_i*f_i%3C4%2Bp%5ET_i%20%5Cqquad%20%5Cforall%20%5C%20i" alt="b_i*f_i&lt;4+p^T_i \qquad \forall \ i" />
</center>




<center>
<img src="https://tex.s2cms.ru/svg/%7Cf_i-s_i%7C%20-%20(t_i*M)%20%5Cleq%20p_i%5EF%20%5Cqquad%20%5Cforall%20%5C%20i" alt="|f_i-s_i| - (t_i*M) \leq p_i^F \qquad \forall \ i" />
</center>
<center>
<img src="https://tex.s2cms.ru/svg/-(s_i-s_%7Bi%2B1%7D)(f_i-f_%7Bi%2B1%7D)%5Cleq%20M*p%5E%7BBC%7D_i%20%5Cqquad%20%5Cforall%20%5C%20i%20%3C%20n-1" alt="-(s_i-s_{i+1})(f_i-f_{i+1})\leq M*p^{BC}_i \qquad \forall \ i &lt; n-1" />
</center>
<center>
<img src="https://tex.s2cms.ru/svg/f_i%20%2B%20f_%7Bi%2B1%7D%20%2B%20f_%7Bi%2B2%7D%20%5Cgeq%205%20%5Cqquad%20%5Cforall%20%5C%20i%20%3C%20n-2" alt="f_i + f_{i+1} + f_{i+2} \geq 5 \qquad \forall \ i &lt; n-2" />
</center>
<center>
<img src="https://tex.s2cms.ru/svg/%7Cf_i-f_%7Bi%2B1%7D%7C%20%5Cgeq%201%20%5Cqquad%20%5Cforall%20%5C%20i%20%3C%20n-1" alt="|f_i-f_{i+1}| \geq 1 \qquad \forall \ i &lt; n-1" />
</center>



An explanation of this model as well as other information about this project can be found in <a href="http://www.mattskarha.com/assets/docs/RHFingerings.pdf">this paper.</a>

# Using this on your own music

If you would like to use this model to determine RH fingerings for your own music, simply download the Python rhfingerings.py file. At the beginning of the code, there is a dictionary *s*. This dictionary is where one would input the ordered sequence of strings to be played. Use the following notation for each string:

- e string: 1
- B string: 2
- G string: 3
- D string: 4
- A string: 5
- E string: 6

Simply run the Python code and it will generate the .lp file that can then be used with Gurobi Optimizer to determine the optimal fingerings for your music. 
