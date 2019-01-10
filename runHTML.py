import webbrowser
import time

def htmlwrite(filename, var1, var2, var3, var4):
    f = open(filename, 'w')

    message = """
    <!DOCTYPE html>

    <html lang="en">
    <head>
        <meta charset="UTF-8" http-equiv="refresh" content="5">

        <!script src = "\htmlDisplay.js">
        <!/script>
        <title>SIOTTest</title>
        <link rel="stylesheet" href = "new.css">
    </head>
    <body >

        <p class="Title"> SIOT Coursework</p>
        <p class="author"> Ben Pheifer</p>
        <p class="Title"> Travel Times From My Home In Dublin</p>

        <p class="updates">School Travel Time = %d s</p>
        <p class="updates">Work Travel Time = %d s</p>
        <p class="updates">Uni Travel Time = %d s</p>
        <p class="updates">Holiday Travel Time = %d s</p>


        <div class = "map">
            <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                 viewBox="0 0 1280 1024" xml:space="preserve">
                <style type="text/css">
                .st0{fill:none;stroke:#FFFF;stroke-width:3;stroke-linecap:bevel;stroke-miterlimit:10;}
                </style>
                <g id="School" >

                    <path class="st0" d="M972.5,265.5l-16-13c20-14.9,31.8-29.9,39-41c8.3-12.9,8.2-17.1,17-29c11.4-15.3,23.1-23.7,39-35
                        c15.2-10.9,30.7-21.9,54-30c15.3-5.3,29.2-7.7,43-10c13-2.2,24-3.3,32-4"></path>
                    <path class="st0" d="M1180.5,103.5l25,18c2.3,2.3,5.3,6,6,11c0.5,3.5-0.6,4.6-2,12c-1.3,6.8-2.4,12.6-1,19c0.8,3.5,2,6.3,3,8"></path>
                    <line class="st0" x1="1211.5" y1="171.5" x2="1223.5" y2="165.5"></line>

                </g>
                <g id="Work">

                    <path class="st0" d="M971.6,266.1L955.7,253c-9.2,5.3-17.1,9.2-23.1,11.9c-5.5,2.5-9,3.9-13,2.9c-4.9-1.1-5.4-4.4-11-8.1
                        c-5.7-3.8-11.3-4.3-21-5.1c-11.6-1-11.5,1.1-19-0.1c-7-1.1-7.6-3.1-23-10.1c-14.9-6.8-21.8-8.5-25-9.1c-6.1-1.3-10.4-2.1-16-1.1
                        c-8.7,1.6-14.4,6.6-17,8.9c-4.7,4.2-6.6,7.7-10.1,13c-9.2,13.8-12.7,14-22.1,26.9c-3.9,5.3-8,12.8-13,23.5"></path>
                    <line class="st0" x1="742.5" y1="306.5" x2="710.5" y2="306.5"></line>

                </g>
                <g id="Holiday">

                        <line class="st0" x1="972.5" y1="265.5" x2="956.5" y2="252.5"></line>
                        <path class="st0" d="M919.5,267.5c-4.5-37.3,7.6-40.3,0-79c-0.5-2.6-0.8-5.9-2-10c-0.7-2.3-2.4-7.6-6-13c-6.6-9.8-12.2-8.4-15-16
                            c-1.9-5.1-0.2-8-3-11c-2.8-3-7.4-3.3-11-3"></path>
                        <path class="st0" d="M882.5,135.5l59-73c-4.9,0.3-12.2,0-20-3c-9.3-3.6-12.9-8.7-20-14c-11-8.1-21.8-10.2-36-13
                            c-21.2-4.1-38.3-1.7-44-1c-66.2,8.6-133.4,4.9-200,9c-79.8,5-89.6,5.3-110,12c-8.3,2.7-50,16.9-93,54c-82.4,71-92,158.7-91,163
                            c0,0.2,0.5,1.9,0,4c-0.4,1.7-1.8,4.4-4,5c-2.6,0.7-3.9-2.2-8-3c-3.1-0.6-5.6,0.5-7,1c-9.2,3.3-26.8,0.4-29,0
                            c-15.4-2.5-15.1-9-34-14c-7-1.9-13.5-3.6-21-3c-17.4,1.4-23,14-42,27c-10.8,7.4-35.4,24.1-58,18c-16.1-4.3-34.6-21.1-40-26
                            c-2.5-2.3-9.3-8.6-20-12c-4.4-1.4-7.9-1.8-10-2c-17.6-1.8-42.8-2-51-2"></path>
                        <line class="st0" x1="3.5" y1="262.5" x2="35.5" y2="242.5"></line>
                        <line class="st0" x1="3.5" y1="262.5" x2="35.5" y2="282.5"></line>
                        <path class="st0" d="M972.6,265.1L956.7,252c-9.2,5.3-17.1,9.2-23.1,11.9c-5.4,2.5-10.7,5.4-14.1,3.6"></path>

                </g>
                <g id="University">

                    <path class="st0" d="M971.6,267.1L955.7,254c-9.2,5.3-17.1,9.2-23.1,11.9c-5.4,2.5-9.6,4.7-13,2.9c-2-1-3.2-3.1-8.1-6.3
                        c0,0-1.4-0.9-2.9-1.7c-7.2-4-15-4.6-21-5.1c-11.6-1-11.5,1.1-19-0.1c-7-1.1-7.6-3.1-23-10.1c-10.9-5-10.2-5-10.2-4.9
                        c0,0.1-0.9-0.1-1-0.1c-1-0.2-2.5,5-4,7c-2.6,3.7-8.8,2.6-13,3c-5.4,0.5-12.8,4-21,17"></path>
                    <line class="st0" x1="796.5" y1="267.5" x2="825.5" y2="295.5"></line>
                    <line class="st0" x1="818.5" y1="309.5" x2="825.5" y2="295.5"></line>
                    <line class="st0" x1="818.5" y1="335.5" x2="818.5" y2="309.5"></line>
                    <line class="st0" x1="850.5" y1="344.5" x2="818.5" y2="335.5"></line>
                    <line class="st0" x1="863.5" y1="355.5" x2="850.5" y2="344.5"></line>
                    <path class="st0" d="M898.5,507.5c-1-3.2-2.8-7.9-6-13c-2.7-4.4-4.4-5.6-6-9c-2.7-5.7-2.1-10.6-2-16c0.3-11.9-1.7-21.2-4-32
                        c-2.1-9.7-4.6-16.9-6-21c-3.6-10.2-5.4-15.5-9-21c-3.2-4.9-10-13.5-24-20c7.3-6.7,14.7-13.3,22-20"></path>
                    <line class="st0" x1="898.5" y1="507.5" x2="889.5" y2="517.5"></line>
                    <line class="st0" x1="880.5" y1="514.5" x2="889.5" y2="517.5"></line>
                    <line class="st0" x1="863.5" y1="513.5" x2="880.5" y2="514.5"></line>
                    <line class="st0" x1="850.5" y1="522.5" x2="863.5" y2="513.5"></line>
                    <line class="st0" x1="829.5" y1="521.5" x2="850.5" y2="522.5"></line>

                </g>
            </svg>
        </div>
                <img src="powered_by_google_on_non_white.png">

    </body>
    </html>

    """ % (var1, var2, var3, var4)
    f.truncate(0)
    f.write(message)
    f.close()

#htmlwrite("new.html",1,1)
#webbrowser.open_new_tab("new.html")
i = 1
a = 2
b = 2
c = 3251
d = 8523
#while True:
    #print "up"
    #a += i
    #b += 2*i
    #htmlwrite("new.html", a, b, c, d)
    #time.sleep(3)
#filename = 'file:///Users/Ben/Documents/SIoT/Python/' + 'new.html'
#chrome.open_new_tab(filename)
