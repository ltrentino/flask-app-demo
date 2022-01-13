d3.select("#get_passengers").on("click", ()=>{
    d3.json("/api/names").then(data => {
        data.passengers.forEach(row =>{
            d3.select("#passenger_list").append("li").text(row.name)
        })
    })
})