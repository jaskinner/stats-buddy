import {Component} from '@angular/core';
import {Observable} from "rxjs";
import { HttpClient } from '@angular/common/http';
import {catchError} from "rxjs/operators";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(private http: HttpClient) {
  }

  term = 'teams';
  teams = this.showTeams()

  /* GET heroes whose name contains search term */
  searchTeams(term: string): Observable<any> {
    term = term.trim();

    let teamsURL = `//localhost:8080/` + term;
    return this.http.get(teamsURL);
  };

  showTeams() {
    this.searchTeams(this.term)
      .subscribe(resp => {
        // access the body directly, which is typed as `Config`.
        this.teams = { ... resp.body };
      });
  }

}
