class Request {

    get(url) {
      return fetch(url)
      .then((res) => res.json());
    }
    
    authGet(url, auth_token) {
      return fetch(url, {
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': "Bearer " + auth_token
        }
      })
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
          return res.json()
        });
    }

    authPost(url, payload, auth_token){
        return fetch(url, {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + auth_token
        },
          body: JSON.stringify(payload)
        })
        .then((res) => {
            return res.json()
          });
      }

      put(url, payload, auth_token){
        return fetch(url, {
          method: "PUT",
          headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + auth_token
          },
          body: JSON.stringify(payload)
        })
        .then((res) => res.json());
      }

}

export default Request;