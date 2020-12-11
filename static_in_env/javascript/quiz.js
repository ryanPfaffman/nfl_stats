const choose_qb = document.getElementById('choose_qb');
const choose_rb = document.getElementById('choose_rb');
const choose_def = document.getElementById('choose_def')

const which_list = document.getElementById('user_1');

const hello_quiz_button = document.getElementById('hello_quiz_button');

hello_quiz = () => {
  console.log(which_list.value);
  if (which_list.value == "Passing") {
    choose_qb.style.display = "block";
    hello_quiz_button.removeEventListener('click', hello_quiz);
    hello_quiz_button.addEventListener('click', broke);
  } else if (which_list.value == "Rushing") {
  choose_rb.style.display = "block";
  hello_quiz_button.removeEventListener('click', hello_quiz);
  hello_quiz_button.addEventListener('click', broke);
} else if (which_list.value == "Defense") {
  choose_def.style.display = "block";
  hello_quiz_button.removeEventListener('click', hello_quiz);
  hello_quiz_button.addEventListener('click', broke);
} else {
  alert("Invalid Input. Try again");
}
}

hello_quiz_button.addEventListener('click', hello_quiz);

which_list.addEventListener('keyup', function(event) {
  if (event.keyCode === 13) {
    hello_quiz_button.click();
    hello_quiz_button.style.backgroundColor = "rgb(215,211,211)";
    hello_quiz_button.addEventListener('mouseover', function() {
      hello_quiz_button.style.backgroundColor = 'red';
    })
    hello_quiz_button.addEventListener('mouseleave', function() {
      hello_quiz_button.style.backgroundColor = "rgb(215,211,211)";
    })
  }
})

which_list.addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
    hello_quiz_button.style.backgroundColor = "red";
  }
})

const which_qb_stat = document.getElementById('qb_input');
const which_rb_stat = document.getElementById('rb_input');
const which_def_stat = document.getElementById('def_input');

const qb_button = document.getElementById('qb_button');
const rb_button = document.getElementById('rb_button');
const def_button = document.getElementById('def_button');

//Quarterbacks

//qb_pass_yds
const qb_pass_yds_div = document.getElementById('qb_pass_yds');

const answer_qb_pass_yds = document.getElementById('answer_qb_pass_yds');

const pass_yds_num_1 = document.getElementById('pass_yds_user_1');
const pass_yds_num_2 = document.getElementById('pass_yds_user_2');
const pass_yds_num_3 = document.getElementById('pass_yds_user_3');
const pass_yds_num_4 = document.getElementById('pass_yds_user_4');
const pass_yds_num_5 = document.getElementById('pass_yds_user_5');

const answer_qb_pass_yds_row = document.getElementById('answer_qb_pass_yds_row');

//pass_yds_per_att
const qb_yds_att_div = document.getElementById('qb_pass_yds_att');

const answer_qb_yds_att = document.getElementById('answer_qb_pass_yds_att');

const pass_yds_att_num_1 = document.getElementById('pass_yds_att_user_1');
const pass_yds_att_num_2 = document.getElementById('pass_yds_att_user_2');
const pass_yds_att_num_3 = document.getElementById('pass_yds_att_user_3');
const pass_yds_att_num_4 = document.getElementById('pass_yds_att_user_4');
const pass_yds_att_num_5 = document.getElementById('pass_yds_att_user_5');

const answer_qb_yds_att_row = document.getElementById('answer_qb_yds_att_row');

//pass_att
const qb_att_div = document.getElementById('qb_pass_att');

const answer_qb_att = document.getElementById('answer_qb_pass_att');

const qb_att_num_1 = document.getElementById('qb_att_user_1');
const qb_att_num_2 = document.getElementById('qb_att_user_2');
const qb_att_num_3 = document.getElementById('qb_att_user_3');
const qb_att_num_4 = document.getElementById('qb_att_user_4');
const qb_att_num_5 = document.getElementById('qb_att_user_5');

const answer_qb_att_row = document.getElementById('answer_qb_att_row');

//pass_cmp
const qb_cmp_div = document.getElementById('qb_pass_cmp');

const answer_qb_cmp = document.getElementById('answer_qb_pass_cmp');

const qb_cmp_num_1 = document.getElementById('qb_cmp_user_1');
const qb_cmp_num_2 = document.getElementById('qb_cmp_user_2');
const qb_cmp_num_3 = document.getElementById('qb_cmp_user_3');
const qb_cmp_num_4 = document.getElementById('qb_cmp_user_4');
const qb_cmp_num_5 = document.getElementById('qb_cmp_user_5');

const answer_qb_cmp_row = document.getElementById('answer_qb_cmp_row');

//pass_cmp_perc
const qb_cmp_perc_div = document.getElementById('qb_pass_cmp_perc');

const answer_qb_cmp_perc = document.getElementById('answer_qb_pass_cmp_perc');

const qb_cmp_perc_num_1 = document.getElementById('qb_cmp_perc_user_1');
const qb_cmp_perc_num_2 = document.getElementById('qb_cmp_perc_user_2');
const qb_cmp_perc_num_3 = document.getElementById('qb_cmp_perc_user_3');
const qb_cmp_perc_num_4 = document.getElementById('qb_cmp_perc_user_4');
const qb_cmp_perc_num_5 = document.getElementById('qb_cmp_perc_user_5');

const answer_qb_cmp_perc_row = document.getElementById('answer_qb_cmp_perc_row');

//pass_td
const qb_td_div = document.getElementById('qb_pass_td');

const answer_qb_td = document.getElementById('answer_qb_pass_td');

const qb_td_num_1 = document.getElementById('qb_td_user_1');
const qb_td_num_2 = document.getElementById('qb_td_user_2');
const qb_td_num_3 = document.getElementById('qb_td_user_3');
const qb_td_num_4 = document.getElementById('qb_td_user_4');
const qb_td_num_5 = document.getElementById('qb_td_user_5');

const answer_qb_td_row = document.getElementById('answer_qb_td_row');

//pass_int
const qb_int_div = document.getElementById('qb_pass_int');

const answer_qb_int = document.getElementById('answer_qb_pass_int');

const qb_int_num_1 = document.getElementById('qb_int_user_1');
const qb_int_num_2 = document.getElementById('qb_int_user_2');
const qb_int_num_3 = document.getElementById('qb_int_user_3');
const qb_int_num_4 = document.getElementById('qb_int_user_4');
const qb_int_num_5 = document.getElementById('qb_int_user_5');

const answer_qb_int_row = document.getElementById('answer_qb_int_row');

//qb_rating
const qb_rating_div = document.getElementById('qb_pass_rating');

const answer_qb_rating = document.getElementById('answer_qb_pass_rating');

const qb_rating_num_1 = document.getElementById('qb_rating_user_1');
const qb_rating_num_2 = document.getElementById('qb_rating_user_2');
const qb_rating_num_3 = document.getElementById('qb_rating_user_3');
const qb_rating_num_4 = document.getElementById('qb_rating_user_4');
const qb_rating_num_5 = document.getElementById('qb_rating_user_5');

const answer_qb_rating_row = document.getElementById('answer_qb_rating_row');

//pass_1st
const qb_1st_div = document.getElementById('qb_pass_1st');

const answer_qb_1st = document.getElementById('answer_qb_pass_1st');

const qb_1st_num_1 = document.getElementById('qb_1st_user_1');
const qb_1st_num_2 = document.getElementById('qb_1st_user_2');
const qb_1st_num_3 = document.getElementById('qb_1st_user_3');
const qb_1st_num_4 = document.getElementById('qb_1st_user_4');
const qb_1st_num_5 = document.getElementById('qb_1st_user_5');

const answer_qb_1st_row = document.getElementById('answer_qb_1st_row');

//pass_1st_%
const qb_1st_perc_div = document.getElementById('qb_pass_1st_perc');

const answer_qb_1st_perc = document.getElementById('answer_qb_pass_1st_perc');

const qb_1st_perc_num_1 = document.getElementById('qb_1st_perc_user_1');
const qb_1st_perc_num_2 = document.getElementById('qb_1st_perc_user_2');
const qb_1st_perc_num_3 = document.getElementById('qb_1st_perc_user_3');
const qb_1st_perc_num_4 = document.getElementById('qb_1st_perc_user_4');
const qb_1st_perc_num_5 = document.getElementById('qb_1st_perc_user_5');

const answer_qb_1st_perc_row = document.getElementById('answer_qb_1st_perc_row');

//pass_20+
const qb_20_div = document.getElementById('qb_pass_20+');

const answer_qb_20 = document.getElementById('answer_qb_pass_20+');

const qb_20_num_1 = document.getElementById('qb_20+_user_1');
const qb_20_num_2 = document.getElementById('qb_20+_user_2');
const qb_20_num_3 = document.getElementById('qb_20+_user_3');
const qb_20_num_4 = document.getElementById('qb_20+_user_4');
const qb_20_num_5 = document.getElementById('qb_20+_user_5');

const answer_qb_20_row = document.getElementById('answer_qb_20+_row');

//pass_40+
const qb_40_div = document.getElementById('qb_pass_40+');

const answer_qb_40 = document.getElementById('answer_qb_pass_40+');

const qb_40_num_1 = document.getElementById('qb_40+_user_1');
const qb_40_num_2 = document.getElementById('qb_40+_user_2');
const qb_40_num_3 = document.getElementById('qb_40+_user_3');
const qb_40_num_4 = document.getElementById('qb_40+_user_4');
const qb_40_num_5 = document.getElementById('qb_40+_user_5');

const answer_qb_40_row = document.getElementById('answer_qb_40+_row');

//pass_long
const qb_long_div = document.getElementById('qb_pass_long');

const answer_qb_long = document.getElementById('answer_qb_pass_long');

const qb_long_num_1 = document.getElementById('qb_long_user_1');
const qb_long_num_2 = document.getElementById('qb_long_user_2');
const qb_long_num_3 = document.getElementById('qb_long_user_3');
const qb_long_num_4 = document.getElementById('qb_long_user_4');
const qb_long_num_5 = document.getElementById('qb_long_user_5');

const answer_qb_long_row = document.getElementById('answer_qb_long_row');

//pass_sack
const qb_sack_div = document.getElementById('qb_pass_sack');

const answer_qb_sack = document.getElementById('answer_qb_pass_sack');

const qb_sack_num_1 = document.getElementById('qb_sack_user_1');
const qb_sack_num_2 = document.getElementById('qb_sack_user_2');
const qb_sack_num_3 = document.getElementById('qb_sack_user_3');
const qb_sack_num_4 = document.getElementById('qb_sack_user_4');
const qb_sack_num_5 = document.getElementById('qb_sack_user_5');

const answer_qb_sack_row = document.getElementById('answer_qb_sack_row');

//pass_sack
const qb_sack_yds_div = document.getElementById('qb_pass_sack_yds');

const answer_qb_sack_yds = document.getElementById('answer_qb_pass_sack_yds');

const qb_sack_yds_num_1 = document.getElementById('qb_sack_yds_user_1');
const qb_sack_yds_num_2 = document.getElementById('qb_sack_yds_user_2');
const qb_sack_yds_num_3 = document.getElementById('qb_sack_yds_user_3');
const qb_sack_yds_num_4 = document.getElementById('qb_sack_yds_user_4');
const qb_sack_yds_num_5 = document.getElementById('qb_sack_yds_user_5');

const answer_qb_sack_yds_row = document.getElementById('answer_qb_sack_yds_row');

//Running Backs

//rb_rush_yds
const rb_yds_div = document.getElementById('rb_yds');

const answer_rb_rush_yds = document.getElementById('answer_rb_rush_yds');
const answer_rb_rush_yds_row = document.getElementById('answer_rb_rush_yds_row');
answer_rb_rush_yds_row.style.display = "none";

const play_again = document.getElementById('play_again');
const play_again_button = document.getElementById('play_again_button')

const rb_yds_num_1 = document.getElementById('rb_yds_user_1');
const rb_yds_num_2 = document.getElementById('rb_yds_user_2');
const rb_yds_num_3 = document.getElementById('rb_yds_user_3');
const rb_yds_num_4 = document.getElementById('rb_yds_user_4');
const rb_yds_num_5 = document.getElementById('rb_yds_user_5');


//rb_att
const rb_att_div = document.getElementById('rb_att');

const answer_rb_att = document.getElementById('answer_rb_att');

const rb_att_num_1 = document.getElementById('rb_att_user_1');
const rb_att_num_2 = document.getElementById('rb_att_user_2');
const rb_att_num_3 = document.getElementById('rb_att_user_3');
const rb_att_num_4 = document.getElementById('rb_att_user_4');
const rb_att_num_5 = document.getElementById('rb_att_user_5');

const answer_rb_att_row = document.getElementById('answer_rb_att_row');

//rb_yds_att
const rb_yds_att_div = document.getElementById('rb_yds_att');

const answer_rb_yds_att = document.getElementById('answer_rb_yds_att');

const rb_yds_att_num_1 = document.getElementById('rb_yds_att_user_1');
const rb_yds_att_num_2 = document.getElementById('rb_yds_att_user_2');
const rb_yds_att_num_3 = document.getElementById('rb_yds_att_user_3');
const rb_yds_att_num_4 = document.getElementById('rb_yds_att_user_4');
const rb_yds_att_num_5 = document.getElementById('rb_yds_att_user_5');

const answer_rb_yds_att_row = document.getElementById('answer_rb_yds_att_row');

//rb_td
const rb_td_div = document.getElementById('rb_td');

const answer_rb_td = document.getElementById('answer_rb_td');

const rb_td_num_1 = document.getElementById('rb_td_user_1');
const rb_td_num_2 = document.getElementById('rb_td_user_2');
const rb_td_num_3 = document.getElementById('rb_td_user_3');
const rb_td_num_4 = document.getElementById('rb_td_user_4');
const rb_td_num_5 = document.getElementById('rb_td_user_5');

const answer_rb_td_row = document.getElementById('answer_rb_td_row');

//rb_20
const rb_20_div = document.getElementById('rb_20');

const answer_rb_20 = document.getElementById('answer_rb_20');

const rb_20_num_1 = document.getElementById('rb_20_user_1');
const rb_20_num_2 = document.getElementById('rb_20_user_2');
const rb_20_num_3 = document.getElementById('rb_20_user_3');
const rb_20_num_4 = document.getElementById('rb_20_user_4');
const rb_20_num_5 = document.getElementById('rb_20_user_5');

const answer_rb_20_row = document.getElementById('answer_rb_20_row');

//rb_40
const rb_40_div = document.getElementById('rb_40');

const answer_rb_40 = document.getElementById('answer_rb_40');

const rb_40_num_1 = document.getElementById('rb_40_user_1');
const rb_40_num_2 = document.getElementById('rb_40_user_2');
const rb_40_num_3 = document.getElementById('rb_40_user_3');
const rb_40_num_4 = document.getElementById('rb_40_user_4');
const rb_40_num_5 = document.getElementById('rb_40_user_5');

const answer_rb_40_row = document.getElementById('answer_rb_40_row');

//rb_long
const rb_long_div = document.getElementById('rb_long');

const answer_rb_long = document.getElementById('answer_rb_long');

const rb_long_num_1 = document.getElementById('rb_long_user_1');
const rb_long_num_2 = document.getElementById('rb_long_user_2');
const rb_long_num_3 = document.getElementById('rb_long_user_3');
const rb_long_num_4 = document.getElementById('rb_long_user_4');
const rb_long_num_5 = document.getElementById('rb_long_user_5');

const answer_rb_long_row = document.getElementById('answer_rb_long_row');

//rb_first
const rb_first_div = document.getElementById('rb_first');

const answer_rb_first = document.getElementById('answer_rb_first');

const rb_first_num_1 = document.getElementById('rb_first_user_1');
const rb_first_num_2 = document.getElementById('rb_first_user_2');
const rb_first_num_3 = document.getElementById('rb_first_user_3');
const rb_first_num_4 = document.getElementById('rb_first_user_4');
const rb_first_num_5 = document.getElementById('rb_first_user_5');

const answer_rb_first_row = document.getElementById('answer_rb_first_row');

//rb_first%
const rb_first_perc_div = document.getElementById('rb_first_perc');

const answer_rb_first_perc = document.getElementById('answer_rb_first_perc');

const rb_first_perc_num_1 = document.getElementById('rb_first_perc_user_1');
const rb_first_perc_num_2 = document.getElementById('rb_first_perc_user_2');
const rb_first_perc_num_3 = document.getElementById('rb_first_perc_user_3');
const rb_first_perc_num_4 = document.getElementById('rb_first_perc_user_4');
const rb_first_perc_num_5 = document.getElementById('rb_first_perc_user_5');

const answer_rb_first_perc_row = document.getElementById('answer_rb_first_perc_row');

//rb_fumbles
const rb_fumbles_div = document.getElementById('rb_fumbles');

const answer_rb_fumbles = document.getElementById('answer_rb_fumbles');

const rb_fumbles_num_1 = document.getElementById('rb_fumbles_user_1');
const rb_fumbles_num_2 = document.getElementById('rb_fumbles_user_2');
const rb_fumbles_num_3 = document.getElementById('rb_fumbles_user_3');
const rb_fumbles_num_4 = document.getElementById('rb_fumbles_user_4');
const rb_fumbles_num_5 = document.getElementById('rb_fumbles_user_5');

const answer_rb_fumbles_row = document.getElementById('answer_rb_fumbles_row');

//Defense

//def_yds
const def_yds_div = document.getElementById('def_yds');

const answer_def_yds = document.getElementById('answer_def_yds');

const def_yds_num_1 = document.getElementById('def_yds_user_1');
const def_yds_num_2 = document.getElementById('def_yds_user_2');
const def_yds_num_3 = document.getElementById('def_yds_user_3');
const def_yds_num_4 = document.getElementById('def_yds_user_4');
const def_yds_num_5 = document.getElementById('def_yds_user_5');

const answer_def_yds_row = document.getElementById('answer_def_yds_row');

//def_yds_g
const def_yds_g_div = document.getElementById('def_yds_g');

const answer_def_yds_g = document.getElementById('answer_def_yds_g');

const def_yds_g_num_1 = document.getElementById('def_yds_g_user_1');
const def_yds_g_num_2 = document.getElementById('def_yds_g_user_2');
const def_yds_g_num_3 = document.getElementById('def_yds_g_user_3');
const def_yds_g_num_4 = document.getElementById('def_yds_g_user_4');
const def_yds_g_num_5 = document.getElementById('def_yds_g_user_5');

const answer_def_yds_g_row = document.getElementById('answer_def_yds_g_row');

//def_pass_yds
const def_pass_yds_div = document.getElementById('def_pass_yds');

const answer_def_pass_yds = document.getElementById('answer_def_pass_yds');

const def_pass_yds_num_1 = document.getElementById('def_pass_yds_user_1');
const def_pass_yds_num_2 = document.getElementById('def_pass_yds_user_2');
const def_pass_yds_num_3 = document.getElementById('def_pass_yds_user_3');
const def_pass_yds_num_4 = document.getElementById('def_pass_yds_user_4');
const def_pass_yds_num_5 = document.getElementById('def_pass_yds_user_5');

const answer_def_pass_yds_row = document.getElementById('answer_def_pass_yds_row');

//def_pass_yds_g
const def_pass_yds_g_div = document.getElementById('def_pass_yds_g');

const answer_def_pass_yds_g = document.getElementById('answer_def_pass_yds_g');

const def_pass_yds_g_num_1 = document.getElementById('def_pass_yds_g_user_1');
const def_pass_yds_g_num_2 = document.getElementById('def_pass_yds_g_user_2');
const def_pass_yds_g_num_3 = document.getElementById('def_pass_yds_g_user_3');
const def_pass_yds_g_num_4 = document.getElementById('def_pass_yds_g_user_4');
const def_pass_yds_g_num_5 = document.getElementById('def_pass_yds_g_user_5');

const answer_def_pass_yds_g_row = document.getElementById('answer_def_pass_yds_g_row');

//def_rush_yds
const def_rush_yds_div = document.getElementById('def_rush_yds');

const answer_def_rush_yds = document.getElementById('answer_def_rush_yds');

const def_rush_yds_num_1 = document.getElementById('def_rush_yds_user_1');
const def_rush_yds_num_2 = document.getElementById('def_rush_yds_user_2');
const def_rush_yds_num_3 = document.getElementById('def_rush_yds_user_3');
const def_rush_yds_num_4 = document.getElementById('def_rush_yds_user_4');
const def_rush_yds_num_5 = document.getElementById('def_rush_yds_user_5');

const answer_def_rush_yds_row = document.getElementById('answer_def_rush_yds_row');

//def_rush_yds_g
const def_rush_yds_g_div = document.getElementById('def_rush_yds_g');

const answer_def_rush_yds_g = document.getElementById('answer_def_rush_yds_g');

const def_rush_yds_g_num_1 = document.getElementById('def_rush_yds_g_user_1');
const def_rush_yds_g_num_2 = document.getElementById('def_rush_yds_g_user_2');
const def_rush_yds_g_num_3 = document.getElementById('def_rush_yds_g_user_3');
const def_rush_yds_g_num_4 = document.getElementById('def_rush_yds_g_user_4');
const def_rush_yds_g_num_5 = document.getElementById('def_rush_yds_g_user_5');

const answer_def_rush_yds_g_row = document.getElementById('answer_def_rush_yds_g_row');

//def_points
const def_points_div = document.getElementById('def_points');

const answer_def_points = document.getElementById('answer_def_points');

const def_points_num_1 = document.getElementById('def_points_user_1');
const def_points_num_2 = document.getElementById('def_points_user_2');
const def_points_num_3 = document.getElementById('def_points_user_3');
const def_points_num_4 = document.getElementById('def_points_user_4');
const def_points_num_5 = document.getElementById('def_points_user_5');

const answer_def_points_row = document.getElementById('answer_def_points_row');

//def_points_g
const def_points_g_div = document.getElementById('def_points_g');

const answer_def_points_g = document.getElementById('answer_def_points_g');

const def_points_g_num_1 = document.getElementById('def_points_g_user_1');
const def_points_g_num_2 = document.getElementById('def_points_g_user_2');
const def_points_g_num_3 = document.getElementById('def_points_g_user_3');
const def_points_g_num_4 = document.getElementById('def_points_g_user_4');
const def_points_g_num_5 = document.getElementById('def_points_g_user_5');

const answer_def_points_g_row = document.getElementById('answer_def_points_g_row');


const play_game = (stat_div, answer_string, answer_row, user_1, user_2, user_3, user_4, user_5) => {
  stat_div.style.display = "block";

  user_1.onclick = () => {
    if (answer_string.innerHTML.includes(user_1.innerHTML)) {
      answer_row.style.display = "block";
      play_again.style.display = "block";
    } else {
      alert('Incorrect');
    }
  }
  user_2.onclick = () => {
    if (answer_string.innerHTML.includes(user_2.innerHTML)) {
      answer_row.style.display = "block";
      play_again.style.display = "block";
      } else {
        alert('Incorrect');
      }
  }
  user_3.onclick = () => {
    if (answer_string.innerHTML.includes(user_3.innerHTML)) {
      answer_row.style.display = "block";
      play_again.style.display = "block";
    } else {
      alert('Incorrect');
    }
  }
  user_4.onclick = () => {
    if (answer_string.innerHTML.includes(user_4.innerHTML)) {
      answer_row.style.display = "block";
      play_again.style.display = "block";
    } else {
      alert('Incorrect');
    }
  }
  user_5.onclick = () => {
    if (answer_string.innerHTML.includes(user_5.innerHTML)){
      answer_row.style.display = "block";
      play_again.style.display = "block";
    } else {
      alert('Incorrect');
    }
  }
}

const qb_quiz = () => {
  if (which_qb_stat.value == 'Passing Yards') {
    play_game(qb_pass_yds_div, answer_qb_pass_yds, answer_qb_pass_yds_row, pass_yds_num_1, pass_yds_num_2, pass_yds_num_3, pass_yds_num_4, pass_yds_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Passing Yards Per Att') {
    play_game(qb_yds_att_div, answer_qb_yds_att, answer_qb_yds_att_row, pass_yds_att_num_1, pass_yds_att_num_2, pass_yds_att_num_3, pass_yds_att_num_4, pass_yds_att_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Att') {
    play_game(qb_att_div, answer_qb_att, answer_qb_att_row, qb_att_num_1, qb_att_num_2, qb_att_num_3, qb_att_num_4, qb_att_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Completions') {
    play_game(qb_cmp_div, answer_qb_cmp, answer_qb_cmp_row, qb_cmp_num_1, qb_cmp_num_2, qb_cmp_num_3, qb_cmp_num_4, qb_cmp_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Completion %') {
    play_game(qb_cmp_perc_div, answer_qb_cmp_perc, answer_qb_cmp_perc_row, qb_cmp_perc_num_1, qb_cmp_perc_num_2, qb_cmp_perc_num_3, qb_cmp_perc_num_4, qb_cmp_perc_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'TD') {
    play_game(qb_td_div, answer_qb_td, answer_qb_td_row, qb_td_num_1, qb_td_num_2, qb_td_num_3, qb_td_num_4, qb_td_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'INT') {
    play_game(qb_int_div, answer_qb_int, answer_qb_int_row, qb_int_num_1, qb_int_num_2, qb_int_num_3, qb_int_num_4, qb_int_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'QB Rating') {
    play_game(qb_rating_div, answer_qb_rating, answer_qb_rating_row, qb_rating_num_1, qb_rating_num_2, qb_rating_num_3, qb_rating_num_4, qb_rating_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'First Downs') {
    play_game(qb_1st_div, answer_qb_1st, answer_qb_1st_row, qb_1st_num_1, qb_1st_num_2, qb_1st_num_3, qb_1st_num_4, qb_1st_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'First Down %') {
    play_game(qb_1st_perc_div, answer_qb_1st_perc, answer_qb_1st_perc_row, qb_1st_perc_num_1, qb_1st_perc_num_2, qb_1st_perc_num_3, qb_1st_perc_num_4, qb_1st_perc_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == '20+') {
    play_game(qb_20_div, answer_qb_20, answer_qb_20_row, qb_20_num_1, qb_20_num_2, qb_20_num_3, qb_20_num_4, qb_20_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == '40+') {
    play_game(qb_40_div, answer_qb_40, answer_qb_40_row, qb_40_num_1, qb_40_num_2, qb_40_num_3, qb_40_num_4, qb_40_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Long') {
    play_game(qb_long_div, answer_qb_long, answer_qb_long_row, qb_long_num_1, qb_long_num_2, qb_long_num_3, qb_long_num_4, qb_long_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Sacks') {
    play_game(qb_sack_div, answer_qb_sack, answer_qb_sack_row, qb_sack_num_1, qb_sack_num_2, qb_sack_num_3, qb_sack_num_4, qb_sack_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else if (which_qb_stat.value == 'Sack Yards') {
    play_game(qb_sack_yds_div, answer_qb_sack_yds, answer_qb_sack_yds_row, qb_sack_yds_num_1, qb_sack_yds_num_2, qb_sack_yds_num_3, qb_sack_yds_num_4, qb_sack_yds_num_5);
    qb_button.removeEventListener('click', qb_quiz);
    qb_button.addEventListener('click', broke);
  } else {
    alert("Invalid Input. Try Again");
  }
}

qb_button.addEventListener('click', qb_quiz);

which_qb_stat.addEventListener('keyup', function(event) {
  if (event.keyCode === 13) {
    qb_button.click();
    qb_button.style.backgroundColor = "rgb(215,211,211)";
    qb_button.addEventListener('mouseover', function() {
      qb_button.style.backgroundColor = 'red';
    })
    qb_button.addEventListener('mouseleave', function() {
      qb_button.style.backgroundColor = "rgb(215,211,211)";
    })
  }
})

which_qb_stat.addEventListener('keydown', function(event){
  if (event.keyCode === 13) {
    qb_button.style.backgroundColor = 'red';
  }
})

const rb_quiz = () => {
  if (which_rb_stat.value == "Rushing Yards") {
    play_game(rb_yds_div, answer_rb_rush_yds, answer_rb_rush_yds_row, rb_yds_num_1, rb_yds_num_2, rb_yds_num_3, rb_yds_num_4, rb_yds_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "Att") {
    play_game(rb_att_div, answer_rb_att, answer_rb_att_row, rb_att_num_1, rb_att_num_2, rb_att_num_3, rb_att_num_4, rb_att_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "Rushing Yards Per Att") {
    play_game(rb_yds_att_div, answer_rb_yds_att, answer_rb_yds_att_row, rb_yds_att_num_1, rb_yds_att_num_2, rb_yds_att_num_3, rb_yds_att_num_4, rb_yds_att_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "TD") {
    play_game(rb_td_div, answer_rb_td, answer_rb_td_row, rb_td_num_1, rb_td_num_2, rb_td_num_3, rb_td_num_4, rb_td_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "20+") {
    play_game(rb_20_div, answer_rb_20, answer_rb_20_row, rb_20_num_1, rb_20_num_2, rb_20_num_3, rb_20_num_4, rb_20_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "40+") {
    play_game(rb_40_div, answer_rb_40, answer_rb_40_row, rb_40_num_1, rb_40_num_2, rb_40_num_3, rb_40_num_4, rb_40_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "Long") {
    play_game(rb_long_div, answer_rb_long, answer_rb_long_row, rb_long_num_1, rb_long_num_2, rb_long_num_3, rb_long_num_4, rb_long_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "First Downs") {
    play_game(rb_first_div, answer_rb_first, answer_rb_first_row, rb_first_num_1, rb_first_num_2, rb_first_num_3, rb_first_num_4, rb_first_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "First Down %") {
    play_game(rb_first_perc_div, answer_rb_first_perc, answer_rb_first_perc_row, rb_first_perc_num_1, rb_first_perc_num_2, rb_first_perc_num_3, rb_first_perc_num_4, rb_first_perc_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else if (which_rb_stat.value == "Fumbles") {
    play_game(rb_fumbles_div, answer_rb_fumbles, answer_rb_fumbles_row, rb_fumbles_num_1, rb_fumbles_num_2, rb_fumbles_num_3, rb_fumbles_num_4, rb_fumbles_num_5);
    rb_button.removeEventListener('click', rb_quiz);
    rb_button.addEventListener('click', broke);
  } else {
    alert("Invalid Input. Try again");
  }

}

rb_button.addEventListener('click',rb_quiz);

which_rb_stat.addEventListener('keyup', function(event) {
  if (event.keyCode === 13) {
    rb_button.click();
    rb_button.style.backgroundColor = "rgb(215,211,211)";
    rb_button.addEventListener('mouseover', function() {
      rb_button.style.backgroundColor = 'red';
    })
    rb_button.addEventListener('mouseleave', function() {
      rb_button.style.backgroundColor = "rgb(215,211,211)";
    })
  }
})

which_rb_stat.addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
    rb_button.style.backgroundColor = "red";
  }
})

const def_quiz = () => {
  if (which_def_stat.value == "Yards") {
    play_game(def_yds_div, answer_def_yds, answer_def_yds_row, def_yds_num_1, def_yds_num_2, def_yds_num_3, def_yds_num_4, def_yds_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value == "Yards Per Game") {
    play_game(def_yds_g_div, answer_def_yds_g, answer_def_yds_g_row, def_yds_g_num_1, def_yds_g_num_2, def_yds_g_num_3, def_yds_g_num_4, def_yds_g_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value == "Passing Yards") {
    play_game(def_pass_yds_div, answer_def_pass_yds, answer_def_pass_yds_row, def_pass_yds_num_1, def_pass_yds_num_2, def_pass_yds_num_3, def_pass_yds_num_4, def_pass_yds_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value == "Passing yards per game") {
    play_game(def_pass_yds_g_div, answer_def_pass_yds_g, answer_def_pass_yds_g_row, def_pass_yds_g_num_1, def_pass_yds_g_num_2, def_pass_yds_g_num_3, def_pass_yds_g_num_4, def_pass_yds_g_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value.toLowerCase() == "rushing yards") {
    play_game(def_rush_yds_div, answer_def_rush_yds, answer_def_rush_yds_row, def_rush_yds_num_1, def_rush_yds_num_2, def_rush_yds_num_3, def_rush_yds_num_4, def_rush_yds_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value.toLowerCase() == "rushing yards per game") {
    play_game(def_rush_yds_g_div, answer_def_rush_yds_g, answer_def_rush_yds_g_row, def_rush_yds_g_num_1, def_rush_yds_g_num_2, def_rush_yds_g_num_3, def_rush_yds_g_num_4, def_rush_yds_g_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value.toLowerCase() == "points") {
    play_game(def_points_div, answer_def_points, answer_def_points_row, def_points_num_1, def_points_num_2, def_points_num_3, def_points_num_4, def_points_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else if (which_def_stat.value.toLowerCase() == "points per game") {
    play_game(def_points_g_div, answer_def_points_g, answer_def_points_g_row, def_points_g_num_1, def_points_g_num_2, def_points_g_num_3, def_points_g_num_4, def_points_g_num_5)
    def_button.removeEventListener('click', def_quiz);
    def_button.addEventListener('click', broke);
  } else {
    alert("Invalid Input. Try again");
  }
}


def_button.addEventListener('click', def_quiz)

which_def_stat.addEventListener('keyup', function(event) {
  if (event.keyCode === 13) {
    def_button.click();
    def_button.style.backgroundColor = "rgb(215,211,211)";
    def_button.addEventListener('mouseover', function() {
      def_button.style.backgroundColor = 'red';
    })
    def_button.addEventListener('mouseleave', function() {
      def_button.style.backgroundColor = "rgb(215,211,211)";
    })
  }
})

which_def_stat.addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
    def_button.style.backgroundColor = "red";
  }
})

const reload = () => {
  location.reload();
}

play_again_button.addEventListener('click', reload);

const broke = () => {
  alert("Invalid");
}
