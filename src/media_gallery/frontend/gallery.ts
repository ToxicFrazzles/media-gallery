class GalleryWidget extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback(){
        this.attachShadow({mode: "open"});
        let self = this;
        fetch("/gallery/list/", {method: "POST"})
            .then(response => {
                return response.json()
            })
            .then(json => {
                console.log(json);
                for(let data of json.list){
                    let newImg = document.createElement("img");
                    newImg.src = data[0];
                    newImg.alt = data[1];
                    self.shadowRoot.appendChild(newImg);
                }
            })
    }
}

customElements.define("gallery-widget", GalleryWidget);