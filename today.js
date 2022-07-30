class today
{
  constructor()
  {
    // Year:2000, Month:0-11, Day:1-30, Hour:0-24, Mins:60, Secs:60
    this.td = new Date() 


    //td pieces
    this.year = this.td.getFullYear()
    this.month = this.months[this.td.getMonth()]
    this.day = this.td.getDate()
   
  }
  

    months =
    [
      "JAN",
      "FEB",
      "MAR",
      "APR",
      "MAY",
      "JUN",
      "JUL",
      "AUG",
      "SEP",
      "OCT",
      "NOV",
      "DEC",
    ]

  get output()  {    return `${this.day}${this.month}${this.year}`  }
  
}