function submitAnswers(answers,pMarks,nMarks){
var total = answers.length;
var score = 0;
var choice = [];
for(var i = 0; i < total; i++){
  choice[i] = document.forms["testForm"]["q"+(i+1)].value;
}
for(i = 0; i < total; i++){
if(choice[i] == (answers[i] + "\n")){
  score+=pMarks;
}
else if(choice[i]==''){
  continue;
}
else{
  score-=nMarks;
}
}
alert("You scored " + score + " out of " + (total*pMarks));

return false;
}
