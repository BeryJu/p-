import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'pyazo-page-gallery',
  templateUrl: './page-gallery.component.html',
  styleUrls: ['./page-gallery.component.scss']
})
export class PageGalleryComponent implements OnInit {

  urlList = [
    "https://s-media-cache-ak0.pinimg.com/564x/1f/4c/93/1f4c93b0816e4277ef7d882ef24c0d10.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/23/d2/ec/23d2ec5d9afe03438a29c3ff3b007b60.jpg",
    "https://s-media-cache-ak0.pinimg.com/236x/19/12/f7/1912f73796ec5107a6cc7ede0b917f9f.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/1b/b6/48/1bb648c481df070f0a6b4a9f14fc3b9f.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/3c/63/06/3c630674a71fd32541e41365953e902e.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/78/41/3f/78413ff949ace8c2c85e3a53ac93a340.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/83/59/d8/8359d80c708fc500916824dfcdc8cd51.jpg",
    "https://s-media-cache-ak0.pinimg.com/236x/a8/85/cf/a885cfbe15d5e2de4ee725a25c109cfa.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/58/54/0c/58540c8382dcd5ee976d61f6fa6be2a3.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/79/4f/1b/794f1b3ca6ef74b4ef851d2d5414f56e.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/e7/a4/f6/e7a4f6053aa41a6fe7b53bf0df90435d.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/d1/3d/71/d13d7133c77b3f68086baca33f803725.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/b6/5f/0a/b65f0ad3b4af916cbafd20b3dc200efd.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/71/8c/25/718c25a080fc2ebe1223a389343e35e5.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/24/68/09/2468093368e0220d6b71cee55ee78030.jpg",
    "https://s-media-cache-ak0.pinimg.com/236x/c8/22/5b/c8225b2c3d16cf65bdcda37f00ab8596.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/91/c9/e7/91c9e76bb090b1b494fdce67ec3819ee.jpg",
    "https://s-media-cache-ak0.pinimg.com/236x/59/56/b9/5956b9caed0d1041eb486b34e4bbbbb5.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/9f/b1/32/9fb1329bb0c2cd400a1226ab913eb061.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/4a/67/f5/4a67f52634f10f42b81c0df5bc43f53d.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/3d/3e/eb/3d3eebba4288e2e8435c54fc723e57a1.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/f9/37/df/f937df0d6e504968f7f4e19938a35f6d.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/b2/b5/a0/b2b5a09209336ea9b3a8adfab28414a8.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/26/e6/14/26e614fba77c47c54246ca143dbe65fa.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/aa/fb/9e/aafb9e3e0a9e78b1afc6bbb08ef26e0f.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/79/6b/ac/796bac332a6ed15e38027c09f049c9f4.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/57/c6/7b/57c67b46d484a977d5e8b3bc4f28f311.jpg",
    "https://s-media-cache-ak0.pinimg.com/236x/35/b5/6f/35b56fa84737eadee2114d1773130a3e.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/77/82/23/77822379a2b1b48046a4be3a1944ae6e.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/f9/96/ef/f996ef0332737e850d1fae3275721d78.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/13/92/71/139271ccdb77c3f141cb45ee4bd49f80.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/7f/3b/77/7f3b77c5cc4b4bd6166c04ef6495952a.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/a6/12/b8/a612b8d912abe4904533298885986d33.jpg",
    "https://s-media-cache-ak0.pinimg.com/564x/fb/73/3b/fb733b1f8ef605370fb8f257dfc19b77.jpg",
  ];

  galleryId: string;

  constructor(private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.galleryId = this.activatedRoute.snapshot.paramMap.get('id');
  }

}
