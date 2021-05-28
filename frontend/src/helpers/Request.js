class Request {

    get(url) {
      return fetch(url)
      .then((res) => res.json());
    }

    delete(url) {
      return fetch(url, {
        method: "DELETE",
        headers: {'Content-Type': 'application/json'}
      })
    }

    post(url, payload){
      return fetch(url, {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      })
      .then((res) => {
          console.log(res.status)
          return res.json()
        });
    }
    
    authPost(url, payload){
        return fetch(url, {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        })
        .then((res) => {
            if (res.status === 200){
                return res.json()
            }
        });
    }
}

export default Request;